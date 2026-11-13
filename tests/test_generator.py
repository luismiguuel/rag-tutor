"""Testes unitários para app/generator.py."""

from unittest.mock import MagicMock, patch

import pytest

MENSAGEM_RECUSA = "Não encontrei essa informação nos documentos disponíveis."


# ---------- Fixtures ---------- #

def _criar_contextos(distancias: list[float]) -> list[dict]:
    """Cria uma lista de contextos simulados com as distâncias fornecidas."""
    return [
        {
            "texto": f"Conteúdo do trecho {i}",
            "origem": f"doc-{i}.md",
            "secao": f"Seção {i}",
            "distancia": d,
        }
        for i, d in enumerate(distancias)
    ]


# ---------- Recusa: lista vazia ---------- #

@patch("app.generator.GEMINI_API_KEY", "fake-key")
def test_gerar_resposta_contextos_vazios():
    """Retorna mensagem de recusa quando não há contextos."""
    from app.generator import gerar_resposta

    resultado = gerar_resposta("O que é ML?", [])
    assert resultado == MENSAGEM_RECUSA


# ---------- Recusa: todos acima do threshold ---------- #

@patch("app.generator.GEMINI_API_KEY", "fake-key")
def test_gerar_resposta_todos_acima_distancia_maxima():
    """Retorna recusa quando todos os contextos excedem DISTANCIA_MAXIMA."""
    from app.generator import gerar_resposta

    contextos = _criar_contextos([0.5, 0.6, 0.9])
    resultado = gerar_resposta("pergunta qualquer", contextos)
    assert resultado == MENSAGEM_RECUSA


# ---------- Filtragem de contextos relevantes ---------- #

@patch("app.generator.GEMINI_API_KEY", "fake-key")
@patch("app.generator.genai")
def test_gerar_resposta_filtra_contextos_relevantes(mock_genai):
    """O prompt deve conter somente contextos com distância <= 0.35."""
    from app.generator import gerar_resposta

    mock_resposta = MagicMock()
    mock_resposta.text = "Resposta gerada pelo modelo."
    mock_genai.Client.return_value.models.generate_content.return_value = (
        mock_resposta
    )

    contextos = _criar_contextos([0.10, 0.35, 0.50, 0.80])
    gerar_resposta("O que é ML?", contextos)

    chamada = mock_genai.Client.return_value.models.generate_content
    chamada.assert_called_once()
    prompt_enviado = chamada.call_args[1]["contents"]

    # Os dois primeiros (0.10 e 0.35) devem estar no prompt
    assert "Conteúdo do trecho 0" in prompt_enviado
    assert "Conteúdo do trecho 1" in prompt_enviado
    # Os outros dois (0.50 e 0.80) não devem estar
    assert "Conteúdo do trecho 2" not in prompt_enviado
    assert "Conteúdo do trecho 3" not in prompt_enviado


# ---------- Resposta gerada ---------- #

@patch("app.generator.GEMINI_API_KEY", "fake-key")
@patch("app.generator.genai")
def test_gerar_resposta_retorna_texto_do_modelo(mock_genai):
    """Deve retornar o texto gerado pelo Gemini, com strip."""
    from app.generator import gerar_resposta

    mock_resposta = MagicMock()
    mock_resposta.text = "  Resposta do tutor.  "
    mock_genai.Client.return_value.models.generate_content.return_value = (
        mock_resposta
    )

    contextos = _criar_contextos([0.15])
    resultado = gerar_resposta("O que é ML?", contextos)
    assert resultado == "Resposta do tutor."


# ---------- Resposta vazia do modelo ---------- #

@patch("app.generator.GEMINI_API_KEY", "fake-key")
@patch("app.generator.genai")
def test_gerar_resposta_modelo_retorna_vazio(mock_genai):
    """Deve levantar RuntimeError quando o Gemini retorna texto vazio."""
    from app.generator import gerar_resposta

    mock_resposta = MagicMock()
    mock_resposta.text = ""
    mock_genai.Client.return_value.models.generate_content.return_value = (
        mock_resposta
    )

    contextos = _criar_contextos([0.20])
    with pytest.raises(RuntimeError, match="não retornou"):
        gerar_resposta("pergunta qualquer", contextos)


@patch("app.generator.GEMINI_API_KEY", "fake-key")
@patch("app.generator.genai")
def test_gerar_resposta_modelo_retorna_none(mock_genai):
    """Deve levantar RuntimeError quando o Gemini retorna None."""
    from app.generator import gerar_resposta

    mock_resposta = MagicMock()
    mock_resposta.text = None
    mock_genai.Client.return_value.models.generate_content.return_value = (
        mock_resposta
    )

    contextos = _criar_contextos([0.20])
    with pytest.raises(RuntimeError, match="não retornou"):
        gerar_resposta("pergunta qualquer", contextos)


# ---------- Sem GEMINI_API_KEY ---------- #

@patch("app.generator.GEMINI_API_KEY", None)
def test_gerar_resposta_sem_api_key():
    """Deve levantar ValueError quando a chave não existe."""
    from app.generator import gerar_resposta

    contextos = _criar_contextos([0.20])
    with pytest.raises(ValueError, match="GEMINI_API_KEY"):
        gerar_resposta("pergunta qualquer", contextos)


@patch("app.generator.GEMINI_API_KEY", "")
def test_gerar_resposta_com_api_key_vazia():
    """String vazia também deve ser tratada como ausente."""
    from app.generator import gerar_resposta

    contextos = _criar_contextos([0.20])
    with pytest.raises(ValueError, match="GEMINI_API_KEY"):
        gerar_resposta("pergunta qualquer", contextos)


# ---------- Threshold confirmado ---------- #

def test_distancia_maxima_vale_035():
    """Confirma que o threshold de distância no módulo é 0.35."""
    from app.generator import DISTANCIA_MAXIMA

    assert DISTANCIA_MAXIMA == pytest.approx(0.35)
