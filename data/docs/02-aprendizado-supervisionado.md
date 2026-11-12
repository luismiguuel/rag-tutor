# Aprendizado Supervisionado

## Conceito

Aprendizado supervisionado é uma abordagem em que o modelo aprende a partir de exemplos que contêm atributos de entrada e uma resposta conhecida. Durante o treinamento, o algoritmo ajusta seus parâmetros para aproximar as previsões dos rótulos apresentados.

O conjunto de dados pode ser representado por pares de entrada e saída. A entrada contém as features e a saída contém o valor que se deseja prever. Após o treinamento, o modelo deve produzir previsões para entradas que não estavam presentes nos exemplos utilizados.

## Regressão

Regressão é uma tarefa supervisionada em que a variável-alvo é numérica e geralmente contínua. Exemplos incluem previsão de preço de imóveis, temperatura e demanda de produtos.

A regressão linear é um método que representa a relação entre as variáveis de entrada e a saída por uma combinação linear dos atributos. Em sua forma simples, pode ser escrita como uma reta. O treinamento procura encontrar coeficientes que minimizem uma função de erro, como o erro quadrático médio.

A regressão linear é útil como modelo inicial por ser relativamente simples e interpretável. Entretanto, relações reais podem não ser lineares, e a presença de valores extremos ou de atributos muito correlacionados pode afetar o ajuste.

## Classificação

Classificação é uma tarefa supervisionada em que a variável-alvo representa uma categoria. Exemplos incluem identificar se uma mensagem é spam, classificar uma imagem ou prever se uma transação é suspeita.

Na classificação binária existem duas classes, como positivo e negativo. Na classificação multiclasse existem mais de duas categorias possíveis. Alguns algoritmos produzem probabilidades ou pontuações para cada classe, que podem ser convertidas em uma decisão usando um limiar.

O limiar de decisão influencia a quantidade de falsos positivos e falsos negativos. Um limiar não deve ser escolhido automaticamente sem considerar o custo dos diferentes tipos de erro.

## Algoritmos comuns

A regressão linear é utilizada principalmente para problemas de regressão. A regressão logística, apesar do nome, é comumente utilizada para classificação e estima a probabilidade de uma classe.

Árvores de decisão dividem os dados por regras sobre os atributos. Elas podem ser usadas em regressão e classificação. Florestas aleatórias combinam várias árvores treinadas com variações dos dados e das features, buscando reduzir a variância de uma árvore isolada.

K-Nearest Neighbors, ou KNN, realiza previsões considerando os exemplos mais próximos segundo uma medida de distância. Como depende de distâncias, a escala dos atributos pode ser importante.

Máquinas de vetores de suporte, ou SVM, procuram separar classes por uma fronteira com margem ampla. Com funções de kernel, podem representar fronteiras não lineares.

## Função de perda e otimização

A função de perda quantifica o erro entre a previsão do modelo e o valor esperado. O algoritmo de treinamento busca ajustar os parâmetros para reduzir essa perda.

Em regressão, o erro quadrático médio é uma opção comum. Em classificação, a entropia cruzada é frequentemente utilizada. A função de perda usada no treinamento não precisa ser igual à métrica escolhida para comunicar o desempenho final.

## Escolha da abordagem

A escolha entre regressão e classificação depende do tipo de variável-alvo e da pergunta do projeto. Prever um valor numérico é regressão; prever uma categoria é classificação. Antes de selecionar um algoritmo, é importante definir a variável-alvo, entender os dados e estabelecer uma métrica adequada.
