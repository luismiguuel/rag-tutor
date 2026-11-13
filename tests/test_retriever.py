"""Testes unitários para app/retriever.py."""

from unittest.mock import MagicMock, patch

import pytest


# ---------- Fixtures ---------- #

def _criar_resultados_chroma(n: int = 3) -> dict:
    """Cria um retorno simulado do ChromaDB com *n* documentos."""
    return {
        "documents": [[f"Texto do documento {i}" for i in range(n)]],
        "metadatas": [
            [
                {"origem": f"doc-{i}.md", "secao": f"Seção {i}"}
                for i in range(n)
            ]
        ],
        "distances": [[0.1 * (i + 1) for i in range(n)]],
    }


# ---------- Recuperação correta ---------- #

@patch("app.retriever.GEMINI_API_KEY", "fake-key")
@patch("app.retriever.chromadb")
@patch("app.retriever.genai")
def test_recuperar_contexto_retorna_lista_correta(
    mock_genai, mock_chromadb
):
    """Verifica documentos, metadados, distância e ordenação."""
    from app.retriever import recuperar_contexto

    # Mock do Gemini — embedding
    mock_embedding = MagicMock()
    mock_embedding.values = [0.1] * 768
    mock_resposta_embed = MagicMock()
    mock_resposta_embed.embeddings = [mock_embedding]
    mock_genai.Client.return_value.models.embed_content.return_value = (
        mock_resposta_embed
    )

    # Mock do ChromaDB — query
    dados_chroma = _criar_resultados_chroma(3)
    mock_colecao = MagicMock()
    mock_colecao.query.return_value = dados_chroma
    mock_chromadb.PersistentClient.return_value.get_collection.return_value = (
        mock_colecao
    )

    resultado = recuperar_contexto("O que é ML?", quantidade=3)

    assert isinstance(resultado, list)
    assert len(resultado) == 3

    for i, ctx in enumerate(resultado):
        assert ctx["texto"] == f"Texto do documento {i}"
        assert ctx["origem"] == f"doc-{i}.md"
        assert ctx["secao"] == f"Seção {i}"
        assert ctx["distancia"] == pytest.approx(0.1 * (i + 1))


@patch("app.retriever.GEMINI_API_KEY", "fake-key")
@patch("app.retriever.chromadb")
@patch("app.retriever.genai")
def test_recuperar_contexto_quantidade_personalizada(
    mock_genai, mock_chromadb
):
    """O parâmetro *quantidade* é repassado ao query do ChromaDB."""
    from app.retriever import recuperar_contexto

    mock_embedding = MagicMock()
    mock_embedding.values = [0.1] * 768
    mock_resposta_embed = MagicMock()
    mock_resposta_embed.embeddings = [mock_embedding]
    mock_genai.Client.return_value.models.embed_content.return_value = (
        mock_resposta_embed
    )

    dados_chroma = _criar_resultados_chroma(2)
    mock_colecao = MagicMock()
    mock_colecao.query.return_value = dados_chroma
    mock_chromadb.PersistentClient.return_value.get_collection.return_value = (
        mock_colecao
    )

    recuperar_contexto("pergunta qualquer", quantidade=2)

    mock_colecao.query.assert_called_once()
    _, kwargs = mock_colecao.query.call_args
    assert kwargs["n_results"] == 2


# ---------- Sem GEMINI_API_KEY ---------- #

@patch("app.retriever.GEMINI_API_KEY", None)
def test_recuperar_contexto_sem_api_key():
    """Deve levantar ValueError quando a chave não existe."""
    from app.retriever import recuperar_contexto

    with pytest.raises(ValueError, match="GEMINI_API_KEY"):
        recuperar_contexto("pergunta qualquer")


@patch("app.retriever.GEMINI_API_KEY", "")
def test_recuperar_contexto_com_api_key_vazia():
    """String vazia também deve ser tratada como ausente."""
    from app.retriever import recuperar_contexto

    with pytest.raises(ValueError, match="GEMINI_API_KEY"):
        recuperar_contexto("pergunta qualquer")


# ---------- Coleção inexistente ---------- #

@patch("app.retriever.GEMINI_API_KEY", "fake-key")
@patch("app.retriever.chromadb")
@patch("app.retriever.genai")
def test_recuperar_contexto_colecao_inexistente(
    mock_genai, mock_chromadb
):
    """Propaga exceção quando a coleção não existe no ChromaDB."""
    from app.retriever import recuperar_contexto

    mock_embedding = MagicMock()
    mock_embedding.values = [0.1] * 768
    mock_resposta_embed = MagicMock()
    mock_resposta_embed.embeddings = [mock_embedding]
    mock_genai.Client.return_value.models.embed_content.return_value = (
        mock_resposta_embed
    )

    mock_chromadb.PersistentClient.return_value.get_collection.side_effect = (
        Exception("Collection not found")
    )

    with pytest.raises(Exception, match="Collection not found"):
        recuperar_contexto("pergunta qualquer")


# ---------- Resultado vazio ---------- #

@patch("app.retriever.GEMINI_API_KEY", "fake-key")
@patch("app.retriever.chromadb")
@patch("app.retriever.genai")
def test_recuperar_contexto_sem_resultados(
    mock_genai, mock_chromadb
):
    """Retorna lista vazia quando o ChromaDB não encontra nada."""
    from app.retriever import recuperar_contexto

    mock_embedding = MagicMock()
    mock_embedding.values = [0.1] * 768
    mock_resposta_embed = MagicMock()
    mock_resposta_embed.embeddings = [mock_embedding]
    mock_genai.Client.return_value.models.embed_content.return_value = (
        mock_resposta_embed
    )

    mock_colecao = MagicMock()
    mock_colecao.query.return_value = {
        "documents": [[]],
        "metadatas": [[]],
        "distances": [[]],
    }
    mock_chromadb.PersistentClient.return_value.get_collection.return_value = (
        mock_colecao
    )

    resultado = recuperar_contexto("pergunta sem resultados")
    assert resultado == []
