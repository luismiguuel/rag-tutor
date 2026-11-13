import json
import time
from datetime import date
from pathlib import Path

from google.genai import errors

from app.generator import gerar_resposta
from app.retriever import recuperar_contexto


CAMINHO_AVALIACAO = Path("eval/golden_set.json")
CAMINHO_RESULTADOS = Path("eval/results/baseline.json")
CAMINHO_PROGRESSO = Path("eval/results/baseline_progress.json")

MENSAGEM_RECUSA = (
    "Não encontrei essa informação nos documentos disponíveis."
)

QUANTIDADE_RESULTADOS = 5


def carregar_perguntas():
    with open(CAMINHO_AVALIACAO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_json(caminho, dados):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(
            dados,
            arquivo,
            ensure_ascii=False,
            indent=4
        )


def carregar_progresso(perguntas):
    if not CAMINHO_PROGRESSO.exists():
        return []

    with open(CAMINHO_PROGRESSO, "r", encoding="utf-8") as arquivo:
        progresso = json.load(arquivo)

    perguntas_salvas = progresso["perguntas_benchmark"]
    perguntas_atuais = [item["pergunta"] for item in perguntas]

    if perguntas_salvas != perguntas_atuais:
        raise ValueError(
            "O benchmark foi alterado. "
            "Revise ou renomeie baseline_progress.json antes de continuar."
        )

    return progresso["resultados"]


def gerar_com_tentativas(pergunta, contextos):
    for tentativa in range(1, 5):
        try:
            return gerar_resposta(pergunta, contextos)

        except errors.APIError as erro:
            codigo = (
                getattr(erro, "code", None)
                or getattr(erro, "status_code", None)
            )

            if codigo not in [429, 500, 502, 503, 504]:
                raise

            if tentativa == 4:
                raise

            if codigo == 429:
                espera = 65
            else:
                espera = 15 * tentativa

            print(
                f"\nErro temporário {codigo}. "
                f"Nova tentativa em {espera} segundos "
                f"({tentativa}/3)..."
            )

            time.sleep(espera)


def executar_avaliacao():
    perguntas = carregar_perguntas()

    CAMINHO_RESULTADOS.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    resultados = carregar_progresso(perguntas)

    perguntas_concluidas = {
        item["pergunta"] for item in resultados
    }

    print("\nAVALIAÇÃO DO RAG TUTOR")
    print("-" * 50)

    print(
        f"Perguntas já concluídas: "
        f"{len(perguntas_concluidas)}/{len(perguntas)}"
    )

    for i, item in enumerate(perguntas, start=1):
        pergunta = item["pergunta"]

        if pergunta in perguntas_concluidas:
            print(f"\nPergunta {i}: já avaliada. Pulando...")
            continue

        respondível = item["respondível"]
        fontes_esperadas = item["fontes_esperadas"]

        inicio_total = time.perf_counter()

        inicio_recuperacao = time.perf_counter()

        contextos = recuperar_contexto(
            pergunta,
            quantidade=QUANTIDADE_RESULTADOS
        )

        fim_recuperacao = time.perf_counter()

        tempo_recuperacao = (
            fim_recuperacao - inicio_recuperacao
        )

        fontes_encontradas = list({
            contexto["origem"] for contexto in contextos
        })

        acertou_recuperacao = any(
            fonte in fontes_encontradas
            for fonte in fontes_esperadas
        )

        inicio_gerador = time.perf_counter()

        try:
            resposta = gerar_com_tentativas(
                pergunta,
                contextos
            )

        except errors.APIError as erro:
            print(f"\nNão foi possível concluir a pergunta {i}.")
            print(f"Erro da API: {erro}")
            print("O progresso anterior foi preservado.")
            return

        fim_gerador = time.perf_counter()

        tempo_gerador = fim_gerador - inicio_gerador

        recusou = MENSAGEM_RECUSA.lower() in resposta.lower()

        if respondível:
            if recusou:
                resultado = "FALSA RECUSA"
            else:
                resultado = "RESPOSTA GERADA - REVISAR"

        else:
            if recusou:
                resultado = "RECUSA CORRETA"
            else:
                resultado = "RESPOSTA INDEVIDA"

        fim_total = time.perf_counter()
        tempo_total = fim_total - inicio_total

        registro = {
            "pergunta": pergunta,
            "respondível": respondível,
            "resultado": resultado,
            "acertou_recuperacao": acertou_recuperacao,
            "fontes_esperadas": fontes_esperadas,
            "fontes_encontradas": fontes_encontradas,
            "resposta": resposta,
            "tempo_recuperacao_segundos": round(tempo_recuperacao, 4),
            "tempo_gerador_segundos": round(tempo_gerador, 4),
            "tempo_total_segundos": round(tempo_total, 4)
        }

        resultados.append(registro)

        salvar_json(
            CAMINHO_PROGRESSO,
            {
                "perguntas_benchmark": [
                    item["pergunta"] for item in perguntas
                ],
                "resultados": resultados
            }
        )

        print(f"\nPergunta {i}: {pergunta}")
        print(f"Resultado: {resultado}")
        print(f"Tempo de recuperação: {tempo_recuperacao:.2f}s")
        print(f"Tempo do gerador: {tempo_gerador:.2f}s")
        print(f"Tempo total: {tempo_total:.2f}s")
        print(f"Resposta: {resposta[:350]}")
        print("Progresso salvo.")

        if i < len(perguntas):
            time.sleep(20)

    total_respondiveis = sum(
        1 for item in perguntas if item["respondível"]
    )

    total_nao_respondiveis = (
        len(perguntas) - total_respondiveis
    )

    acertos_recuperacao = sum(
        1 for item in resultados
        if item["respondível"] and item["acertou_recuperacao"]
    )

    recusas_corretas = sum(
        1 for item in resultados
        if item["resultado"] == "RECUSA CORRETA"
    )

    falsas_recusas = sum(
        1 for item in resultados
        if item["resultado"] == "FALSA RECUSA"
    )

    hit_rate = (
        acertos_recuperacao / total_respondiveis * 100
        if total_respondiveis else 0
    )

    taxa_recusa = (
        recusas_corretas / total_nao_respondiveis * 100
        if total_nao_respondiveis else 0
    )

    taxa_falsa_recusa = (
        falsas_recusas / total_respondiveis * 100
        if total_respondiveis else 0
    )

    media_recuperacao = sum(
        item["tempo_recuperacao_segundos"]
        for item in resultados
    ) / len(resultados)

    media_gerador = sum(
        item["tempo_gerador_segundos"]
        for item in resultados
    ) / len(resultados)

    media_total = sum(
        item["tempo_total_segundos"]
        for item in resultados
    ) / len(resultados)

    metricas = {
        "hit_rate_at_5": {
            "acertos": acertos_recuperacao,
            "total": total_respondiveis,
            "percentual": round(hit_rate, 2)
        },
        "correct_refusal_rate": {
            "recusas_corretas": recusas_corretas,
            "total": total_nao_respondiveis,
            "percentual": round(taxa_recusa, 2)
        },
        "false_refusal_rate": {
            "falsas_recusas": falsas_recusas,
            "total": total_respondiveis,
            "percentual": round(taxa_falsa_recusa, 2)
        },
        "tempo_medio_recuperacao_segundos": round(media_recuperacao, 4),
        "tempo_medio_gerador_segundos": round(media_gerador, 4),
        "tempo_medio_total_segundos": round(media_total, 4)
    }

    dados_resultado = {
        "projeto": "RAG Tutor",
        "data_avaliacao": date.today().isoformat(),
        "arquivo_benchmark": str(CAMINHO_AVALIACAO),
        "quantidade_resultados": QUANTIDADE_RESULTADOS,
        "total_perguntas": len(perguntas),
        "metricas": metricas,
        "perguntas": resultados
    }

    salvar_json(CAMINHO_RESULTADOS, dados_resultado)

    CAMINHO_PROGRESSO.unlink(missing_ok=True)

    print("\n" + "=" * 50)
    print("RESULTADOS FINAIS")
    print("=" * 50)

    print(f"Hit Rate@{QUANTIDADE_RESULTADOS}: {hit_rate:.2f}%")
    print(f"Correct Refusal Rate: {taxa_recusa:.2f}%")
    print(f"False Refusal Rate: {taxa_falsa_recusa:.2f}%")

    print(f"Tempo médio de recuperação: {media_recuperacao:.2f}s")
    print(f"Tempo médio do gerador: {media_gerador:.2f}s")
    print(f"Tempo médio total: {media_total:.2f}s")

    print(f"\nResultados salvos em: {CAMINHO_RESULTADOS}")


if __name__ == "__main__":
    executar_avaliacao()
