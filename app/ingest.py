import hashlib
import re
from pathlib import Path

import chromadb
from google import genai
from google.genai import types

from app.config import (
    CHROMA_PATH,
    COLLECTION_NAME,
    GEMINI_API_KEY,
    GEMINI_EMBEDDING_MODEL,
)

PASTA_DOCUMENTOS = Path("data/docs")
TAMANHO_CHUNK = 3000
SOBREPOSICAO = 400
TAMANHO_LOTE = 50


def ler_documentos(pasta: Path = PASTA_DOCUMENTOS) -> list[dict]:
    """Lê os arquivos Markdown e identifica a seção de cada parágrafo."""
    documentos = []

    for caminho in sorted(pasta.glob("*.md")):
        conteudo = caminho.read_text(encoding="utf-8")
        secao_atual = "Introdução"

        for bloco in re.split(r"\n\s*\n", conteudo):
            bloco = bloco.strip()

            if not bloco:
                continue

            if bloco.startswith("#"):
                secao_atual = re.sub(r"^#+\s*", "", bloco).strip()
                continue

            documentos.append({
                "texto": bloco,
                "origem": caminho.name,
                "secao": secao_atual,
            })

    return documentos


def dividir_em_chunks(documentos: list[dict]) -> list[dict]:
    """Agrupa parágrafos em chunks com limite de caracteres e sobreposição."""
    chunks = []

    for documento in documentos:
        texto = documento["texto"]
        inicio = 0

        while inicio < len(texto):
            fim = min(inicio + TAMANHO_CHUNK, len(texto))

            # Evita cortar uma frase no meio quando existe pontuação próxima.
            if fim < len(texto):
                ponto = texto.rfind(". ", inicio, fim)
                if ponto > inicio + TAMANHO_CHUNK // 2:
                    fim = ponto + 1

            trecho = texto[inicio:fim].strip()

            if trecho:
                chunks.append({
                    "texto": trecho,
                    "origem": documento["origem"],
                    "secao": documento["secao"],
                })

            if fim >= len(texto):
                break

            inicio = max(fim - SOBREPOSICAO, inicio + 1)

    return chunks


def gerar_embeddings(cliente: genai.Client, textos: list[str]) -> list[list[float]]:
    """Gera um embedding para cada texto recebido."""
    resposta = cliente.models.embed_content(
        model=GEMINI_EMBEDDING_MODEL,
        contents=textos,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT",
        ),
    )

    return [embedding.values for embedding in resposta.embeddings]


def ingerir_documentos() -> int:
    """Reconstrói a coleção do ChromaDB com os documentos atuais."""
    if not GEMINI_API_KEY:
        raise ValueError(
            "GEMINI_API_KEY não configurada. Verifique o arquivo .env."
        )

    documentos = ler_documentos()

    if not documentos:
        raise ValueError(f"Nenhum arquivo Markdown encontrado em {PASTA_DOCUMENTOS}.")

    chunks = dividir_em_chunks(documentos)

    if not chunks:
        raise ValueError("Os documentos foram encontrados, mas nenhum chunk foi gerado.")

    cliente_gemini = genai.Client(api_key=GEMINI_API_KEY)
    cliente_chroma = chromadb.PersistentClient(path=CHROMA_PATH)

    # A coleção é específica deste projeto; recriá-la evita chunks antigos.
    try:
        cliente_chroma.delete_collection(name=COLLECTION_NAME)
    except Exception:
        pass

    colecao = cliente_chroma.create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    for inicio in range(0, len(chunks), TAMANHO_LOTE):
        lote = chunks[inicio:inicio + TAMANHO_LOTE]
        textos = [chunk["texto"] for chunk in lote]
        embeddings = gerar_embeddings(cliente_gemini, textos)

        ids = []
        metadados = []

        for posicao, chunk in enumerate(lote, start=inicio):
            identificador = hashlib.sha256(
                f"{chunk['origem']}:{chunk['secao']}:{posicao}:{chunk['texto']}".encode("utf-8")
            ).hexdigest()

            ids.append(identificador)
            metadados.append({
                "origem": chunk["origem"],
                "secao": chunk["secao"],
                "posicao": posicao,
            })

        colecao.add(
            ids=ids,
            documents=textos,
            embeddings=embeddings,
            metadatas=metadados,
        )

        print(f"Lote processado: {min(inicio + len(lote), len(chunks))}/{len(chunks)}")

    print(f"Ingestão concluída: {len(chunks)} chunks armazenados.")
    return len(chunks)


if __name__ == "__main__":
    ingerir_documentos()
