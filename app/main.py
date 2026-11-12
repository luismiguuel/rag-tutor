from fastapi import FastAPI

from app.generator import gerar_resposta
from app.retriever import recuperar_contexto
from app.schemas import PerguntaRequest, PerguntaResponse

app = FastAPI(
    title="RAG Tutor",
    description="Tutor de Machine Learning baseado em documentos.",
    version="1.0.0",
)

@app.post(
    "/perguntar",
    response_model=PerguntaResponse
)
def perguntar(dados: PerguntaRequest):
    contextos = recuperar_contexto(dados.pergunta)

    resposta = gerar_resposta(
        dados.pergunta,
        contextos
    )

    return PerguntaResponse(
        pergunta=dados.pergunta,
        resposta=resposta
    )