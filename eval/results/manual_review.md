# Revisão Manual dos Resultados do Benchmark — RAG Tutor

## 1. Objetivo da Revisão

Esta revisão manual tem como objetivo avaliar de forma criteriosa e aprofundada a qualidade das respostas geradas pelo pipeline RAG do projeto **RAG Tutor**, registradas em `eval/results/baseline.json`, com base exclusivamente no conjunto de documentos de referência presentes em `data/docs/` e nas perguntas do `eval/golden_set.json`.

O propósito é validar se o sistema:
1. Responde corretamente e com rigor conceitual às dúvidas sobre Machine Learning.
2. Mantém fidelidade estrita às fontes documentais, sem alucinações ou extrapolações não fundamentadas.
3. Fornece respostas completas e contextualizadas conforme solicitado.
4. Cita corretamente os documentos e seções de onde extraiu o conteúdo.
5. Recusa-se de forma precisa e padronizada a responder perguntas fora do domínio coberto pela base de conhecimento.

---

## 2. Critérios de Avaliação

Cada uma das 20 perguntas do benchmark foi avaliada sob quatro dimensões:

- **Correção conceitual:** a resposta está cientificamente e tecnicamente correta de acordo com as definições dos documentos?
- **Fidelidade às fontes:** todas as afirmações são estritamente sustentadas pelos documentos de referência (`data/docs/`), sem inclusão de conhecimento externo ou alucinação?
- **Completude:** a resposta contempla todos os elementos e nuances essenciais demandados pela pergunta e abordados na fonte?
- **Citações:** os nomes de arquivos e seções citados existem, estão formatados adequadamente e correspondem com precisão ao trecho utilizado?

### Categorias de Classificação:
- **`Aprovada`**: resposta correta, estritamente fundamentada nos documentos, com citações adequadas e suficientemente completa.
- **`Aprovada com ressalva`**: resposta essencialmente correta e fundamentada, mas que apresenta omissão parcial, imprecisão secundária, estilo tautológico ou falha menor de formatação de citação.
- **`Reprovada`**: resposta que contém erro conceitual, informação não sustentada pelos documentos (alucinação), omissão importante de componente estrutural da pergunta ou falha relevante no conteúdo gerado.

Para as perguntas não cobertas pela documentação (perguntas 17 a 20), o critério de aprovação exigiu o retorno exato da mensagem padrão:
> `Não encontrei essa informação nos documentos disponíveis.`

---

## 3. Avaliação Individual das Perguntas

As avaliações a seguir estão agrupadas pelos documentos de referência correspondentes a cada tema, preservando a numeração original (1 a 20).

---

### Módulo 1: Introdução ao Machine Learning (`data/docs/01-introducao-ml.md`)

#### Pergunta 1 — O que é Machine Learning?
- **Respondível:** Sim.
- **Fontes esperadas:** `01-introducao-ml.md`.
- **Fontes recuperadas pelo RAG:** `01-introducao-ml.md`, `02-aprendizado-supervisionado.md`.
- **Correção conceitual:** Correta.
- **Fidelidade às fontes:** Alta. Totalmente fundamentada em `01-introducao-ml.md`.
- **Citações:** Precisas e existentes (`[01-introducao-ml.md, O que é Machine Learning]`).
- **Completude:** Excelente. Aborda a definição formal, a diferença entre programação tradicional e aprendizado por exemplos, o conceito de modelo matemático/computacional com exemplo prático (preço de imóveis) e as limitações (regularidades estatísticas vs compreensão humana).
- **Classificação:** **`Aprovada`**

#### Pergunta 2 — Quais são as principais etapas de um projeto de Machine Learning?
- **Respondível:** Sim.
- **Fontes esperadas:** `01-introducao-ml.md`.
- **Fontes recuperadas pelo RAG:** `01-introducao-ml.md`.
- **Correção conceitual:** Correta.
- **Fidelidade às fontes:** Alta. Reproduz fielmente a sequência descrita na seção `Etapas de um projeto de Machine Learning`.
- **Citações:** Precisas (`[01-introducao-ml.md, Etapas de um projeto de Machine Learning]`).
- **Completude:** Completa. Cobre com exatidão as 6 etapas: Definição do problema, Coleta e exploração de dados, Preparação e divisão dos dados, Treinamento do algoritmo, Avaliação de desempenho e Disponibilização/monitoramento.
- **Classificação:** **`Aprovada`**

#### Pergunta 3 — Quais são os tipos de aprendizado em Machine Learning?
- **Respondível:** Sim.
- **Fontes esperadas:** `01-introducao-ml.md`.
- **Fontes recuperadas pelo RAG:** `01-introducao-ml.md`, `03-aprendizado-nao-supervisionado.md`, `02-aprendizado-supervisionado.md`.
- **Correção conceitual:** Correta quanto ao que foi explicado (supervisionado e não supervisionado).
- **Fidelidade às fontes:** Fiel aos trechos apresentados.
- **Citações:** Formatação inconsistente. O modelo removeu a extensão `.md` em todas as citações desta resposta (`[01-introducao-ml, Tipos de aprendizado]`, `[02-aprendizado-supervisionado, Conceito]`, `[03-aprendizado-nao-supervisionado, Conceito]`).
- **Completude:** Incompleta. O documento `01-introducao-ml.md` (seção `Tipos de aprendizado`) divide explicitamente o aprendizado em três tipos: Supervisionado, Não Supervisionado e **Aprendizado por Reforço** (com agente, ambiente, ações e recompensas). A resposta omitiu totalmente o Aprendizado por Reforço.
- **Classificação:** **`Aprovada com ressalva`**

#### Pergunta 4 — Qual é a diferença entre atributos e variável-alvo?
- **Respondível:** Sim.
- **Fontes esperadas:** `01-introducao-ml.md`.
- **Fontes recuperadas pelo RAG:** `01-introducao-ml.md`, `02-aprendizado-supervisionado.md`.
- **Correção conceitual:** Correta.
- **Fidelidade às fontes:** Alta.
- **Citações:** Adequadas (`[01-introducao-ml.md, Dados, atributos e variável-alvo]`, `[01-introducao-ml.md, Tipos de aprendizado]`, `[02-aprendizado-supervisionado.md, Escolha da abordagem; 02-aprendizado-supervisionado.md, Classificação]`).
- **Completude:** Completa. Define atributos (features/características de entrada) e variável-alvo (saída a prever), além de ilustrar como a variável-alvo se manifesta em tarefas de regressão (numérica) e classificação (categórica).
- **Classificação:** **`Aprovada`**

---

### Módulo 2: Aprendizado Supervisionado (`data/docs/02-aprendizado-supervisionado.md`)

#### Pergunta 5 — Qual é a diferença entre regressão e classificação?
- **Respondível:** Sim.
- **Fontes esperadas:** `02-aprendizado-supervisionado.md`.
- **Fontes recuperadas pelo RAG:** `01-introducao-ml.md`, `02-aprendizado-supervisionado.md`.
- **Correção conceitual:** Correta.
- **Fidelidade às fontes:** Alta.
- **Citações:** Precisas e completas com seções existentes (`[02-aprendizado-supervisionado.md, Regressão]`, `[02-aprendizado-supervisionado.md, Escolha da abordagem]`, `[02-aprendizado-supervisionado.md, Algoritmos comuns]`, `[02-aprendizado-supervisionado.md, Função de perda e otimização]`, `[01-introducao-ml.md, Tipos de aprendizado]`).
- **Completude:** Excelente. Diferencia o tipo de variável-alvo (numérica contínua vs categórica), fornece exemplos reais do texto (imóveis, temperatura, demanda vs spam, imagem, fraude), cita algoritmos correspondentes (regressão linear vs logística) e funções de perda típicas (MSE vs entropia cruzada).
- **Classificação:** **`Aprovada`**

#### Pergunta 6 — O que são funções de perda e otimização?
- **Respondível:** Sim.
- **Fontes esperadas:** `02-aprendizado-supervisionado.md`.
- **Fontes recuperadas pelo RAG:** `01-introducao-ml.md`, `02-aprendizado-supervisionado.md`.
- **Correção conceitual:** Correta.
- **Fidelidade às fontes:** Alta.
- **Citações:** Precisas (`[02-aprendizado-supervisionado.md, Função de perda e otimização]`, `[01-introducao-ml.md, Etapas de um projeto de Machine Learning]`, `[02-aprendizado-supervisionado.md, Regressão]`).
- **Completude:** Completa. Define função de perda como quantificadora do erro entre previsão e valor esperado, e otimização como o processo de ajuste de parâmetros do algoritmo para minimizar tal erro.
- **Classificação:** **`Aprovada`**

---

### Módulo 3: Aprendizado Não Supervisionado (`data/docs/03-aprendizado-nao-supervisionado.md`)

#### Pergunta 7 — O que é clustering no aprendizado não supervisionado?
- **Respondível:** Sim.
- **Fontes esperadas:** `03-aprendizado-nao-supervisionado.md`.
- **Fontes recuperadas pelo RAG:** `01-introducao-ml.md`, `03-aprendizado-nao-supervisionado.md`.
- **Correção conceitual:** Correta.
- **Fidelidade às fontes:** Alta.
- **Citações:** Adequadas (`[01-introducao-ml.md, Tipos de aprendizado; 03-aprendizado-nao-supervisionado.md, Conceito]`, `[03-aprendizado-nao-supervisionado.md, Clustering]`).
- **Completude:** Satisfatória. Enquadra o clustering na ausência de rótulos/variável-alvo e define a organização de observações em grupos com base em noções de similaridade segundo atributos e métricas selecionadas.
- **Classificação:** **`Aprovada`**

#### Pergunta 8 — Para que serve a redução de dimensionalidade?
- **Respondível:** Sim.
- **Fontes esperadas:** `03-aprendizado-nao-supervisionado.md`.
- **Fontes recuperadas pelo RAG:** `03-aprendizado-nao-supervisionado.md`.
- **Correção conceitual:** Correta.
- **Fidelidade às fontes:** Alta.
- **Citações:** Precisas (`[03-aprendizado-nao-supervisionado.md, Redução de dimensionalidade]`, `[03-aprendizado-nao-supervisionado.md, Conceito]`).
- **Completude:** Completa. Destaca a representação com menos variáveis preservando informação relevante e elenca todas as finalidades descritas no documento: visualização, redução de custo computacional e suporte à exploração de dados.
- **Classificação:** **`Aprovada`**

---

### Módulo 4: Treinamento e Validação de Modelos (`data/docs/04-treinamento-e-validacao.md`)

#### Pergunta 9 — O que é overfitting e como evitá-lo?
- **Respondível:** Sim.
- **Fontes esperadas:** `04-treinamento-e-validacao.md`.
- **Fontes recuperadas pelo RAG:** `04-treinamento-e-validacao.md`.
- **Correção conceitual:** Correta.
- **Fidelidade às fontes:** Alta.
- **Citações:** Precisas (`[04-treinamento-e-validacao.md, Overfitting]`, `[04-treinamento-e-validacao.md, Viés e variância]`).
- **Completude:** Excelente. Responde aos dois comandos da pergunta: conceitua o sobreajuste aos detalhes e ruídos do treino associado à alta variância e pior desempenho em dados não vistos, e enumera as 5 estratégias indicadas no documento para mitigá-lo (limitar complexidade, regularização, aumento de dados, seleção de atributos e validação adequada).
- **Classificação:** **`Aprovada`**

#### Pergunta 10 — Qual é a diferença entre overfitting e underfitting?
- **Respondível:** Sim.
- **Fontes esperadas:** `04-treinamento-e-validacao.md`.
- **Fontes recuperadas pelo RAG:** `04-treinamento-e-validacao.md`.
- **Correção conceitual:** Correta.
- **Fidelidade às fontes:** Alta.
- **Citações:** Precisas (`[04-treinamento-e-validacao.md, Underfitting]`, `[04-treinamento-e-validacao.md, Viés e variância]`, `[04-treinamento-e-validacao.md, Overfitting]`).
- **Completude:** Completa. Apresenta uma comparação simétrica e bem estruturada entre underfitting (não captura padrões, desempenho ruim em treino e avaliação, alto viés) e overfitting (ajuste excessivo a ruídos, ótimo no treino e ruim em dados não vistos, alta variância).
- **Classificação:** **`Aprovada`**

#### Pergunta 11 — O que é validação cruzada?
- **Respondível:** Sim.
- **Fontes esperadas:** `04-treinamento-e-validacao.md`.
- **Fontes recuperadas pelo RAG:** `04-treinamento-e-validacao.md`.
- **Correção conceitual:** Correta.
- **Fidelidade às fontes:** Alta.
- **Citações:** Precisas e completas (`[04-treinamento-e-validacao.md, Divisão dos dados]`, `[04-treinamento-e-validacao.md, Validação cruzada]`, `[04-treinamento-e-validacao.md, Vazamento de dados]`, `[04-treinamento-e-validacao.md, Parâmetros e hiperparâmetros]`).
- **Completude:** Muito aprofundada. Explica o objetivo em dados pequenos, o funcionamento detalhado do K-Fold clássico, a validação cruzada estratificada para classes desbalanceadas, a integração com pipelines para evitar vazamento em pré-processamentos e o uso na seleção de hiperparâmetros sem comprometer o teste final.
- **Classificação:** **`Aprovada`**

#### Pergunta 12 — O que é vazamento de dados e por que ele é prejudicial?
- **Respondível:** Sim.
- **Fontes esperadas:** `04-treinamento-e-validacao.md`.
- **Fontes recuperadas pelo RAG:** `01-introducao-ml.md`, `04-treinamento-e-validacao.md`.
- **Correção conceitual:** Correta na definição fundamental.
- **Fidelidade às fontes:** Fiel aos trechos literais dos documentos.
- **Citações:** Corretas (`[04-treinamento-e-validacao.md, Vazamento de dados]`, `[01-introducao-ml.md, Dados, atributos e variável-alvo]`).
- **Completude:** Parcial / Ressalva estilística e de profundidade. A resposta conceitua data leakage adequadamente ("informações que não estariam disponíveis no momento real influenciam o treino ou avaliação"). Entretanto, a justificativa de "por que é prejudicial" resultou em uma explicação circular e rasa: *"Ele é prejudicial porque pode prejudicar a avaliação [...] uma vez que o treinamento ou a avaliação são influenciados por dados que não seriam acessíveis na prática"*. Além disso, foram omitidos os exemplos práticos trazidos na seção correspondente do documento `04-treinamento-e-validacao.md` (como usar variável derivada do resultado ou aplicar pré-processamento/padronização em todo o conjunto antes da divisão).
- **Classificação:** **`Aprovada com ressalva`**

---

### Módulo 5: Métricas de Avaliação em Machine Learning (`data/docs/05-metricas-avaliacao.md`)

#### Pergunta 13 — O que é uma matriz de confusão?
- **Respondível:** Sim.
- **Fontes esperadas:** `05-metricas-avaliacao.md`.
- **Fontes recuperadas pelo RAG:** `05-metricas-avaliacao.md`.
- **Correção conceitual:** As definições de FP e FN apresentadas estão corretas.
- **Fidelidade às fontes:** Fiel ao que foi extraído.
- **Citações:** Existente (`[05-metricas-avaliacao.md, Matriz de confusão]`).
- **Completude:** Gravemente incompleta. A pergunta indaga "O que é uma matriz de confusão?". A resposta afirma textualmente que *"Na classificação binária, a matriz de confusão apresenta quatro resultados principais"*, mas na sequência introduz: *"Dois desses resultados são: Falso Positivo (FP) [...] e Falso Negativo (FN) [...]"*, encerrando o texto abruptamente sem mencionar nem explicar os **Verdadeiros Positivos (VP)** e os **Verdadeiros Negativos (VN)**. Como a matriz de confusão é estruturada fundamentalmente sobre os quatro quadrantes de predição cruzada, omitir a totalidade dos acertos (metade da matriz) constitui uma omissão importante que inviabiliza a compreensão conceitual da ferramenta.
- **Classificação:** **`Reprovada`**

#### Pergunta 14 — Qual é a diferença entre precisão e recall?
- **Respondível:** Sim.
- **Fontes esperadas:** `05-metricas-avaliacao.md`.
- **Fontes recuperadas pelo RAG:** `05-metricas-avaliacao.md`.
- **Correção conceitual:** Impecável.
- **Fidelidade às fontes:** Alta.
- **Citações:** Precisas (`[05-metricas-avaliacao.md, Precisão]`, `[05-metricas-avaliacao.md, Recall]`).
- **Completude:** Excelente. Traz as definições teóricas, as fórmulas exatas conforme o documento (`VP / (VP + FP)` e `VP / (VP + FN)`), a interpretação prática de cada uma e uma conclusão clara sintetizando exatidão versus completude na identificação de positivos.
- **Classificação:** **`Aprovada`**

#### Pergunta 15 — O que é F1-score e qual sua relação com precisão e recall?
- **Respondível:** Sim.
- **Fontes esperadas:** `05-metricas-avaliacao.md`.
- **Fontes recuperadas pelo RAG:** `05-metricas-avaliacao.md`.
- **Correção conceitual:** Correta.
- **Fidelidade às fontes:** Alta.
- **Citações:** Precisas (`[05-metricas-avaliacao.md, F1-score]`).
- **Completude:** Completa. Define como média harmônica, esclarece que seu objetivo é o equilíbrio entre precisão e recall e fornece a fórmula matemática correspondente descrita no documento.
- **Classificação:** **`Aprovada`**

#### Pergunta 16 — Quais métricas podem ser utilizadas para avaliar modelos de regressão?
- **Respondível:** Sim.
- **Fontes esperadas:** `05-metricas-avaliacao.md`.
- **Fontes recuperadas pelo RAG:** `02-aprendizado-supervisionado.md`, `05-metricas-avaliacao.md`.
- **Correção conceitual:** Correta.
- **Fidelidade às fontes:** Alta.
- **Citações:** Precisas (`[05-metricas-avaliacao.md, Escolha da métrica]`, `[05-metricas-avaliacao.md, Métricas de regressão]`).
- **Completude:** Completa. Detalha MAE, RMSE e R² (além de referenciar a relação do RMSE com o MSE), explicando interpretação de escala, penalidade de erros e limites de referência.
- **Classificação:** **`Aprovada`**

---

### Módulo 6: Perguntas Sem Resposta nos Documentos (Teste de Recusa)

#### Pergunta 17 — Qual é a capital da França?
- **Respondível:** Não (fora de domínio).
- **Fontes esperadas:** Nenhuma (`[]`).
- **Fontes recuperadas pelo RAG:** Recuperou trechos não relacionados (`02-aprendizado-supervisionado.md`, etc.).
- **Resposta gerada:** *"Não encontrei essa informação nos documentos disponíveis."*
- **Fidelidade e Recusa:** Recusa perfeita e exata. O sistema não utilizou conhecimento prévio externo para responder "Paris".
- **Classificação:** **`Aprovada`** (Recusa correta)

#### Pergunta 18 — Como funciona a fotossíntese nas plantas?
- **Respondível:** Não (fora de domínio).
- **Fontes esperadas:** Nenhuma (`[]`).
- **Resposta gerada:** *"Não encontrei essa informação nos documentos disponíveis."*
- **Fidelidade e Recusa:** Recusa perfeita e exata. O sistema absteve-se de gerar conteúdo biológico ausente da base.
- **Classificação:** **`Aprovada`** (Recusa correta)

#### Pergunta 19 — Quem foi Albert Einstein?
- **Respondível:** Não (fora de domínio).
- **Fontes esperadas:** Nenhuma (`[]`).
- **Resposta gerada:** *"Não encontrei essa informação nos documentos disponíveis."*
- **Fidelidade e Recusa:** Recusa perfeita e exata. O sistema não recorreu a conhecimento enciclopédico externo.
- **Classificação:** **`Aprovada`** (Recusa correta)

#### Pergunta 20 — Como calcular a área de um triângulo?
- **Respondível:** Não (fora de domínio).
- **Fontes esperadas:** Nenhuma (`[]`).
- **Resposta gerada:** *"Não encontrei essa informação nos documentos disponíveis."*
- **Fidelidade e Recusa:** Recusa perfeita e exata. O sistema recusou a fórmula matemática geométrica ausente dos documentos.
- **Classificação:** **`Aprovada`** (Recusa correta)

---

## 4. Análise dos Problemas Encontrados

A análise minuciosa confirmou e aprofundou as hipóteses levantadas na etapa preliminar:

1. **Omissão estrutural grave na Pergunta 13 (Matriz de Confusão):**
   - **Descrição:** O modelo enunciou explicitamente a existência de 4 resultados na classificação binária, mas explicou apenas 2 (Falso Positivo e Falso Negativo), ignorando completamente Verdadeiro Positivo e Verdadeiro Negativo.
   - **Impacto:** Resposta conceitualmente manca e insuficiente para o usuário compreender a matriz. Justifica a reprovação da resposta.
   - **Causa provável:** O gerador truncou o detalhamento ou priorizou os erros na geração da resposta a partir do chunk de texto.

2. **Omissão de paradigma na Pergunta 3 (Tipos de Aprendizado):**
   - **Descrição:** O documento `01-introducao-ml.md` lista três grandes tipos de aprendizado: Supervisionado, Não Supervisionado e Aprendizado por Reforço. O modelo apresentou apenas os dois primeiros.
   - **Falha secundária de citação:** Nesta mesma pergunta, todas as citações perderam a extensão de arquivo (gerando `[01-introducao-ml, Tipos de aprendizado]` em vez de `[01-introducao-ml.md, ...]`).
   - **Impacto:** Resposta incompleta em relação à fonte direta, motivando a aprovação com ressalva.

3. **Superficialidade e circularidade na Pergunta 12 (Vazamento de Dados):**
   - **Descrição:** A explicação sobre por que data leakage é prejudicial foi circular (*"prejudicial porque pode prejudicar a avaliação"*). Foram omitidos os exemplos práticos fornecidos no texto (derivação de variável da resposta e vazamento por pré-processamento global antes da divisão).
   - **Impacto:** Embora correta e livre de alucinações, a resposta carece de completude argumentativa frente à riqueza do texto original.

4. **Pontos fortes observados:**
   - **Alucinação zero:** Em nenhuma das 20 perguntas o modelo inventou fatos ou extrapolou o domínio das fontes.
   - **Comportamento de recusa impecável (100%):** Nas 4 perguntas fora de escopo, o sistema não cedeu à tentação de usar o conhecimento paramétrico do LLM, emitindo exatamente a sentença prescrita pelo protocolo de recusa.
   - **Alta fidelidade técnica em métricas (Perguntas 14, 15 e 16):** As explicações de fórmulas e interpretações de precisão, recall, F1 e regressão foram excelentes.

---

## 5. Resumo Quantitativo da Revisão

| Métrica | Quantidade | Percentual |
| :--- | :---: | :---: |
| **Total de perguntas revisadas** | **20** | **100%** |
| Perguntas Aprovadas (sem ressalvas) | 17 | 85,0% |
| *(das quais são respostas técnicas aprofundadas)* | *13* | *65,0%* |
| *(das quais são recusas padronizadas perfeitas)* | *4* | *20,0%* |
| Perguntas Aprovadas com ressalva | 2 | 10,0% |
| Perguntas Reprovadas | 1 | 5,0% |
| **Taxa de Recusas Corretas (perguntas 17 a 20)** | **4 / 4** | **100,0%** |
| **Taxa de Falsas Recusas (perguntas 1 a 16)** | **0 / 16** | **0,0%** |

### Distribuição por Pergunta:
- **Aprovadas (17):** P1, P2, P4, P5, P6, P7, P8, P9, P10, P11, P14, P15, P16, P17, P18, P19, P20.
- **Aprovadas com ressalva (2):** P3, P12.
- **Reprovadas (1):** P13.

---

## 6. Recomendações de Melhoria para o Sistema

1. **Ajuste no prompt do gerador para respostas completas em enumerações:**
   - Adicionar uma diretriz explícita no system prompt do gerador para que, quando o texto-fonte listar categorias, quadrantes ou etapas (ex.: os 4 quadrantes da matriz de confusão ou os 3 tipos de aprendizado), o gerador garanta a inclusão integral de todos os itens antes de concluir a resposta.
2. **Reforço na formatação de citações:**
   - Padronizar no prompt do gerador a obrigatoriedade da extensão do arquivo na citação (ex.: `[documento.md, Seção]`), prevenindo inconsistências como as observadas na Pergunta 3.
3. **Incentivo à inclusão de exemplos das fontes:**
   - Orientar o gerador a incorporar os exemplos práticos presentes no contexto recuperado quando perguntado "como funciona", "o que é" ou "por que é prejudicial", enriquecendo respostas conceituais como a de data leakage (Pergunta 12).
