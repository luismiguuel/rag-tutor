# Treinamento e Validação de Modelos

## Divisão dos dados

O conjunto de dados costuma ser dividido para separar o ajuste do modelo de sua avaliação. O conjunto de treinamento é utilizado para aprender os parâmetros. O conjunto de validação pode apoiar a escolha de hiperparâmetros e decisões de desenvolvimento. O conjunto de teste deve ser reservado para uma avaliação final, sem orientar repetidamente as escolhas do modelo.

Uma divisão comum é treino, validação e teste, mas as proporções dependem do tamanho e das características do conjunto de dados. Em conjuntos pequenos, validação cruzada pode aproveitar melhor os exemplos disponíveis.

## Parâmetros e hiperparâmetros

Parâmetros são valores aprendidos pelo modelo durante o treinamento, como coeficientes de uma regressão linear. Hiperparâmetros são configurações escolhidas antes ou durante o processo de seleção, como profundidade máxima de uma árvore ou quantidade de vizinhos no KNN.

Ajustar hiperparâmetros usando o conjunto de teste causa vazamento de informação da avaliação final. A seleção deve utilizar dados de validação ou procedimentos de validação cruzada aplicados aos dados de desenvolvimento.

## Overfitting

Overfitting, ou sobreajuste, acontece quando o modelo se ajusta excessivamente aos detalhes e ruídos dos dados de treinamento. Ele pode apresentar desempenho muito bom no treinamento e desempenho significativamente pior em dados não vistos.

Modelos excessivamente complexos, conjuntos pequenos e dados ruidosos podem favorecer o sobreajuste. Estratégias para reduzi-lo incluem limitar a complexidade, regularização, aumento de dados quando apropriado, seleção de atributos e validação adequada.

## Underfitting

Underfitting, ou subajuste, acontece quando o modelo não consegue capturar adequadamente os padrões presentes nos dados. Nesse caso, o desempenho tende a ser ruim tanto no treinamento quanto na avaliação.

Um modelo simples demais, atributos pouco informativos ou treinamento insuficiente podem causar subajuste. Aumentar a capacidade do modelo, melhorar os atributos ou ajustar o processo de treinamento pode ajudar.

## Viés e variância

Viés representa o erro associado a simplificações fortes feitas pelo modelo. Variância representa a sensibilidade do modelo às particularidades da amostra de treinamento. Modelos com viés elevado podem apresentar subajuste; modelos com variância elevada podem apresentar sobreajuste.

O objetivo não é minimizar isoladamente viés ou variância, mas encontrar um equilíbrio que produza boa generalização.

## Validação cruzada

Na validação cruzada K-Fold, os dados são divididos em K partes, chamadas folds. Em cada rodada, uma parte é usada para validação e as demais para treinamento. O processo se repete até que cada parte tenha sido usada para validação uma vez.

O desempenho pode ser resumido pela média e pelo desvio padrão das métricas obtidas nos folds. A média indica o desempenho típico e o desvio padrão informa quanto os resultados variaram entre as divisões.

Na validação cruzada estratificada, as proporções das classes são aproximadamente preservadas em cada fold. Isso é útil em problemas de classificação com classes desbalanceadas.

Quando existem observações relacionadas, como várias medições do mesmo paciente ou várias amostras do mesmo usuário, uma divisão aleatória pode colocar dados relacionados em treino e validação. Nesses casos, divisões por grupos ajudam a evitar vazamento entre os conjuntos.

## Vazamento de dados

Data leakage ocorre quando informações que não estariam disponíveis no momento real da previsão influenciam o treinamento ou a avaliação. Exemplos incluem usar uma variável derivada diretamente do resultado ou ajustar um pré-processamento com todo o conjunto antes da divisão.

Transformações como imputação, padronização e seleção de atributos devem ser ajustadas apenas com os dados de treinamento de cada divisão. Em validação cruzada, isso normalmente é feito por meio de um pipeline executado separadamente em cada fold.
