import chromadb
from google import genai
from google.genai import types

from app.config import (
    CHROMA_PATH,
    COLLECTION_NAME,
    GEMINI_API_KEY,
    GEMINI_EMBEDDING_MODEL,
)


def recuperar_contexto(pergunta: str, quantidade: int = 5) -> list[dict]:
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY não configurada.")

    cliente_gemini = genai.Client(api_key=GEMINI_API_KEY)

    resposta = cliente_gemini.models.embed_content(
        model=GEMINI_EMBEDDING_MODEL,
        contents=pergunta,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY"
        ),
    )

    embedding = resposta.embeddings[0].values

    cliente_chroma = chromadb.PersistentClient(
        path=CHROMA_PATH
    )

    colecao = cliente_chroma.get_collection(
        name=COLLECTION_NAME
    )

    resultados = colecao.query(
        query_embeddings=[embedding],
        n_results=quantidade,
        include=[
            "documents",
            "metadatas",
            "distances",
        ],
    )

    contextos = []

    for i in range(len(resultados["documents"][0])):
        contextos.append({
            "texto": resultados["documents"][0][i],
            "origem": resultados["metadatas"][0][i]["origem"],
            "secao": resultados["metadatas"][0][i]["secao"],
            "distancia": resultados["distances"][0][i],
        })

    return contextos