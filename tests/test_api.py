"""Testes de integração para o endpoint POST /perguntar."""

from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

MENSAGEM_RECUSA = "Não encontrei essa informação nos documentos disponíveis."


# ---------- Requisição válida ---------- #

@patch("app.main.gerar_resposta", return_value="Resposta simulada.")
@patch(
    "app.main.recuperar_contexto",
    return_value=[
        {
            "texto": "Trecho de exemplo",
            "origem": "doc.md",
            "secao": "Seção A",
            "distancia": 0.12,
        }
    ],
)
def test_perguntar_retorna_200(mock_recuperar, mock_gerar):
    """Requisição válida deve retornar HTTP 200."""
    resposta = client.post(
        "/perguntar",
        json={"pergunta": "O que é Machine Learning?"},
    )
    assert resposta.status_code == 200


@patch("app.main.gerar_resposta", return_value="Resposta simulada.")
@patch(
    "app.main.recuperar_contexto",
    return_value=[
        {
            "texto": "Trecho de exemplo",
            "origem": "doc.md",
            "secao": "Seção A",
            "distancia": 0.12,
        }
    ],
)
def test_perguntar_estrutura_json(mock_recuperar, mock_gerar):
    """A resposta deve conter as chaves 'pergunta' e 'resposta'."""
    resposta = client.post(
        "/perguntar",
        json={"pergunta": "O que é Machine Learning?"},
    )
    dados = resposta.json()
    assert "pergunta" in dados
    assert "resposta" in dados
    assert dados["pergunta"] == "O que é Machine Learning?"
    assert dados["resposta"] == "Resposta simulada."


# ---------- Encaminhamento correto ---------- #

@patch("app.main.gerar_resposta", return_value="Resposta do tutor.")
@patch("app.main.recuperar_contexto", return_value=[])
def test_perguntar_encaminha_para_funcoes(mock_recuperar, mock_gerar):
    """A pergunta deve ser encaminhada ao retriever e ao generator."""
    texto = "O que é overfitting?"
    client.post("/perguntar", json={"pergunta": texto})

    mock_recuperar.assert_called_once_with(texto)
    mock_gerar.assert_called_once_with(texto, [])


# ---------- Validação de tamanho mínimo ---------- #

def test_perguntar_rejeita_pergunta_curta():
    """Perguntas com menos de 3 caracteres devem retornar HTTP 422."""
    resposta = client.post(
        "/perguntar",
        json={"pergunta": "ML"},
    )
    assert resposta.status_code == 422


def test_perguntar_rejeita_pergunta_vazia():
    """Pergunta vazia deve retornar HTTP 422."""
    resposta = client.post(
        "/perguntar",
        json={"pergunta": ""},
    )
    assert resposta.status_code == 422


# ---------- Modelo de dados ---------- #

@patch(
    "app.main.gerar_resposta",
    return_value=MENSAGEM_RECUSA,
)
@patch("app.main.recuperar_contexto", return_value=[])
def test_perguntar_resposta_de_recusa(mock_recuperar, mock_gerar):
    """Deve retornar a mensagem padronizada de recusa."""
    resposta = client.post(
        "/perguntar",
        json={"pergunta": "Capital da França?"},
    )
    dados = resposta.json()
    assert dados["resposta"] == MENSAGEM_RECUSA


# ---------- Sem body ---------- #

def test_perguntar_sem_body():
    """Requisição sem corpo deve retornar HTTP 422."""
    resposta = client.post("/perguntar")
    assert resposta.status_code == 422
