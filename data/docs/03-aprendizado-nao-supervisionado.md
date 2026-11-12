# Aprendizado Não Supervisionado

## Conceito

Aprendizado não supervisionado utiliza dados sem rótulos conhecidos para encontrar estruturas ou padrões. O algoritmo recebe atributos de entrada, mas não recebe uma resposta correta para cada observação durante o treinamento.

Essa abordagem é útil quando se deseja explorar conjuntos de dados, descobrir grupos de observações semelhantes ou representar dados com menos dimensões. Os resultados precisam ser interpretados no contexto do problema, pois um agrupamento matemático não garante, por si só, uma categoria com significado prático.

## Clustering

Clustering, ou agrupamento, procura organizar observações em grupos de acordo com alguma noção de similaridade. Observações do mesmo grupo devem ser relativamente semelhantes segundo os atributos e a medida escolhidos.

O K-Means é um algoritmo conhecido de clustering. O usuário define previamente o número K de grupos. O algoritmo atribui cada observação ao centroide mais próximo e recalcula os centroides a partir dos pontos atribuídos. Essas etapas são repetidas até atingir um critério de parada.

O K-Means é relativamente simples, mas pode ser sensível à inicialização, à escala dos atributos e a valores extremos. Também funciona melhor quando os grupos podem ser representados por regiões aproximadamente compactas. A escolha de K influencia o resultado.

O agrupamento hierárquico constrói uma estrutura de grupos em diferentes níveis. Na abordagem aglomerativa, cada observação começa em seu próprio grupo e grupos são unidos progressivamente. A estrutura pode ser visualizada por um dendrograma.

O DBSCAN forma grupos a partir de regiões densas e pode identificar observações isoladas como ruído. Diferentemente do K-Means, não exige informar diretamente o número de grupos, mas depende de parâmetros de vizinhança e densidade.

## Redução de dimensionalidade

Redução de dimensionalidade busca representar os dados com menos variáveis, preservando parte da informação relevante. Isso pode facilitar visualização, reduzir custo computacional e ajudar na exploração de dados.

PCA, ou Análise de Componentes Principais, transforma os atributos originais em componentes não correlacionados que representam direções de maior variância. Os primeiros componentes concentram a maior parte da variância explicada pela transformação.

PCA é sensível à escala dos atributos. Por isso, padronizar as variáveis antes da aplicação pode ser importante quando elas possuem unidades ou amplitudes diferentes. A redução de dimensionalidade também pode descartar informação, então a variância explicada deve ser analisada.

## Similaridade e escala

O resultado de métodos baseados em distância depende da representação dos dados e da métrica escolhida. Se um atributo varia entre zero e um e outro varia entre zero e cem mil, o segundo pode dominar o cálculo de distância.

Padronização e normalização são estratégias para tornar escalas mais comparáveis. A escolha depende da distribuição dos atributos e do algoritmo utilizado.

## Avaliação de agrupamentos

Avaliar clustering é mais difícil quando não existem rótulos verdadeiros. O coeficiente de silhueta compara a proximidade de uma observação com seu próprio grupo e com grupos vizinhos. Valores maiores indicam, em geral, grupos mais separados e coesos.

Uma métrica não substitui a análise do significado dos grupos. É necessário verificar estabilidade, utilidade e coerência com o domínio do problema.
