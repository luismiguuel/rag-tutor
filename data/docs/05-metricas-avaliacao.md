# Métricas de Avaliação em Machine Learning

## Matriz de confusão

Em classificação, a matriz de confusão compara as classes previstas com as classes reais. Na classificação binária, existem quatro resultados principais.

Verdadeiro positivo (VP) ocorre quando o modelo prevê a classe positiva e ela realmente é positiva. Verdadeiro negativo (VN) ocorre quando o modelo prevê a classe negativa e ela realmente é negativa.

Falso positivo (FP) ocorre quando o modelo prevê positivo, mas o valor real é negativo. Falso negativo (FN) ocorre quando o modelo prevê negativo, mas o valor real é positivo.

A interpretação de cada erro depende do contexto. Em detecção de fraude, um falso negativo pode representar uma fraude não identificada. Um falso positivo pode bloquear uma transação legítima.

## Acurácia

Accuracy, ou acurácia, é a proporção de previsões corretas entre todas as previsões. Na classificação binária, é calculada por (VP + VN) / (VP + VN + FP + FN).

A acurácia é fácil de interpretar, mas pode ser enganosa em conjuntos desbalanceados. Se 99% dos exemplos pertencem à classe negativa, um modelo que sempre prevê negativo pode alcançar 99% de acurácia e ainda falhar completamente na identificação da classe positiva.

## Precisão

Precision, ou precisão, é a proporção de previsões positivas que realmente são positivas. É calculada por VP / (VP + FP).

A precisão é relevante quando falsos positivos são especialmente custosos. Por exemplo, em um sistema que encaminha alertas para análise humana, baixa precisão pode gerar muitos alertas incorretos.

Se o modelo não produzir nenhuma previsão positiva, o denominador pode ser zero. Bibliotecas de métricas geralmente definem uma política para esse caso, que deve ser documentada.

## Recall

Recall, também chamado de sensibilidade, é a proporção de exemplos positivos reais que foram identificados corretamente. É calculado por VP / (VP + FN).

Recall é importante quando deixar de identificar um positivo é custoso. Em triagem médica ou detecção de fraude, um recall baixo pode significar muitos casos relevantes não detectados.

## F1-score

F1-score é a média harmônica entre precisão e recall. É calculado por 2 × (precisão × recall) / (precisão + recall).

O F1-score busca equilibrar precisão e recall. Ele não considera diretamente os verdadeiros negativos e pode não ser a melhor métrica para todos os problemas. A escolha deve refletir os custos e objetivos da aplicação.

Em problemas multiclasse, métricas podem ser agregadas por média macro, micro ou ponderada. A média macro calcula a métrica por classe e dá o mesmo peso a cada classe. A média ponderada considera a quantidade de exemplos de cada classe. A média micro agrega as contribuições de todas as classes antes do cálculo.

## Métricas de regressão

MAE, ou erro absoluto médio, calcula a média dos valores absolutos das diferenças entre previsões e valores reais. Sua unidade é a mesma da variável-alvo.

MSE, ou erro quadrático médio, calcula a média dos erros elevados ao quadrado. Como erros grandes recebem penalidade maior, valores extremos podem influenciar bastante o resultado. Sua unidade é o quadrado da unidade original.

RMSE é a raiz quadrada do MSE e retorna à unidade da variável-alvo. Tanto MAE quanto RMSE são métricas em que valores menores indicam menor erro.

R², ou coeficiente de determinação, compara o desempenho do modelo com uma referência baseada na média da variável-alvo. Um valor próximo de um indica que o modelo explica uma grande parte da variação observada segundo essa definição. R² pode ser negativo quando o modelo tem desempenho pior que a referência.

## Escolha da métrica

Não existe uma única métrica ideal para todos os projetos. A métrica deve refletir o objetivo, o tipo de tarefa, o balanceamento das classes e o custo dos erros.

Em classificação desbalanceada, precisão, recall, F1-score e métricas baseadas em curvas podem ser mais informativas que a acurácia isolada. Em regressão, MAE e RMSE ajudam a interpretar o tamanho dos erros, enquanto R² oferece uma comparação relativa com uma referência.
