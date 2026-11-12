# Introdução ao Machine Learning

## O que é Machine Learning

Machine Learning, ou aprendizado de máquina, é uma área da inteligência artificial que desenvolve métodos capazes de identificar padrões em dados e utilizar esses padrões para realizar previsões ou tomar decisões. Em vez de programar manualmente todas as regras para cada situação, fornecemos exemplos a um algoritmo para que ele ajuste um modelo a partir desses dados.

Um modelo é uma representação matemática ou computacional das relações aprendidas durante o treinamento. Depois de treinado, ele pode receber dados que ainda não viu e produzir uma previsão. Por exemplo, um modelo pode estimar o preço de uma casa usando características como área, localização e quantidade de quartos.

Machine Learning não significa que o computador compreende os dados da mesma forma que uma pessoa. O sistema encontra regularidades estatísticas e depende da qualidade dos dados, da escolha do algoritmo e da forma como o problema foi definido.

## Etapas de um projeto de Machine Learning

Um projeto costuma começar pela definição do problema. É necessário entender qual resultado se deseja prever, quais decisões serão tomadas com esse resultado e como o sucesso será medido.

Em seguida, são coletados e explorados os dados. Essa etapa permite identificar tipos de variáveis, valores ausentes, registros duplicados, erros e possíveis relações entre atributos. Depois, os dados são preparados e divididos em conjuntos de treinamento, validação e teste, quando aplicável.

O algoritmo escolhido é treinado usando os dados de treinamento. Seus parâmetros são ajustados para reduzir uma função de perda. O desempenho é avaliado com métricas adequadas ao problema. Por fim, o modelo pode ser disponibilizado para uso e monitorado para identificar mudanças nos dados ou queda de desempenho.

## Tipos de aprendizado

No aprendizado supervisionado, os exemplos usados no treinamento possuem uma resposta conhecida, chamada rótulo ou variável-alvo. O modelo aprende a relacionar os atributos de entrada com essa resposta. Regressão e classificação são tarefas supervisionadas.

No aprendizado não supervisionado, os dados não possuem uma variável-alvo fornecida. O objetivo é encontrar estruturas, agrupamentos ou representações úteis. Clustering é um exemplo dessa categoria.

No aprendizado por reforço, um agente interage com um ambiente, realiza ações e recebe recompensas ou penalidades. O objetivo é aprender uma estratégia que maximize a recompensa acumulada ao longo do tempo.

## Dados, atributos e variável-alvo

Uma observação representa um exemplo do conjunto de dados, como uma casa, um cliente ou uma transação. Os atributos, também chamados de características ou features, descrevem cada observação. A variável-alvo é aquilo que o modelo deve prever em uma tarefa supervisionada.

A escolha dos atributos influencia diretamente o resultado. Atributos irrelevantes, incorretos ou que revelem indiretamente a resposta podem prejudicar a avaliação. Esse último problema é conhecido como vazamento de dados, ou data leakage.

## Limitações e cuidados

Um modelo pode apresentar bom desempenho nos dados usados durante o treinamento e falhar em dados novos. Por isso, avaliar a capacidade de generalização é essencial. Também é importante considerar representatividade dos dados, privacidade, viés, interpretabilidade e consequências das decisões automatizadas.

Machine Learning não substitui a definição cuidadosa do problema. Um algoritmo sofisticado não corrige automaticamente dados ruins nem uma métrica inadequada.
