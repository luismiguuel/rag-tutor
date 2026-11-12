from google import genai
from google.genai import types

from app.config import (
    GEMINI_API_KEY,
    GEMINI_GENERATION_MODEL,
)

DISTANCIA_MAXIMA = 0.35

def gerar_resposta(pergunta: str, contextos: list[dict]) -> str:
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY não configurada.")

    if not contextos:
        return "Não encontrei essa informação nos documentos disponíveis."

    contextos_relevantes = [
        contexto
        for contexto in contextos
        if contexto["distancia"] <= DISTANCIA_MAXIMA
    ]

    if not contextos_relevantes:
        return "Não encontrei essa informação nos documentos disponíveis."

    cliente = genai.Client(api_key=GEMINI_API_KEY)

    contexto_formatado = ""

    for i, contexto in enumerate(contextos_relevantes):
        contexto_formatado += (
            f"\nTrecho {i + 1}\n"
            f"Documento: {contexto['origem']}\n"
            f"Seção: {contexto['secao']}\n"
            f"Conteúdo: {contexto['texto']}\n"
        )

    prompt = f"""
Você é um tutor especializado em Machine Learning.

Sua tarefa é responder à pergunta do usuário utilizando
exclusivamente as informações presentes nos documentos fornecidos.

Regras:
1. Não utilize conhecimentos externos aos documentos.
2. Não invente informações ou referências.
3. Se os documentos não contiverem informações suficientes
   para responder, diga exatamente:
   "Não encontrei essa informação nos documentos disponíveis."
4. Seja claro, didático e objetivo.
5. Sempre indique as fontes utilizadas, informando o documento
   e a seção entre colchetes.

Documentos disponíveis:
{contexto_formatado}

Pergunta do usuário:
{pergunta}

Resposta:
"""

    resposta = cliente.models.generate_content(
        model=GEMINI_GENERATION_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
            max_output_tokens=1024,
        ),
    )

    if not resposta.text:
        raise RuntimeError("O Gemini não retornou uma resposta.")

    return resposta.text.strip()
