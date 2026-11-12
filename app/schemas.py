from pydantic import BaseModel, Field

class PerguntaRequest(BaseModel):
    pergunta: str = Field(
        min_length=3,
        description="Pergunta enviada ao tutor."
    )

class PerguntaResponse(BaseModel):
    pergunta: str
    resposta: str