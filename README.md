# Projeto de Machine Learning - Previsão de Salário

## Objetivo

Desenvolver um modelo de Machine Learning capaz de prever salários com base em características profissionais, como anos de experiência e quantidade de cursos realizados.

## Tecnologias Utilizadas

* Python
* Pandas
* Matplotlib
* Scikit-Learn
* Jupyter Notebook

## Dataset

O conjunto de dados contém as seguintes variáveis:

| Variável    | Descrição                        |
| ----------- | -------------------------------- |
| experiencia | Anos de experiência profissional |
| cursos      | Quantidade de cursos realizados  |
| salario     | Salário mensal (variável alvo)   |

## Etapas do Projeto

### 1. Análise Exploratória

Foram realizadas análises estatísticas utilizando:

* head()
* info()
* describe()
* corr()

### 2. Visualização dos Dados

Foi utilizado um gráfico de dispersão para analisar a relação entre experiência e salário.

### 3. Preparação dos Dados

Separação entre:

* Features (X)

  * experiencia
  * cursos

* Target (y)

  * salario

Divisão dos dados:

* 80% Treino
* 20% Teste

### 4. Treinamento do Modelo

Modelo utilizado:

* Linear Regression

Biblioteca:

```python
from sklearn.linear_model import LinearRegression
```

### 5. Avaliação

Métrica utilizada:

* Mean Absolute Error (MAE)

Objetivo:

Medir o erro médio absoluto entre os valores reais e os valores previstos.

## Resultados

O modelo foi capaz de identificar a relação entre experiência, cursos e salário, realizando previsões para novos registros.

## Aprendizados

Durante este projeto foram aplicados conceitos de:

* Python
* Pandas
* Estatística
* Correlação
* Regressão Linear
* Avaliação de Modelos
* Machine Learning Supervisionado

## Próximos Passos

* Utilizar datasets maiores
* Testar novos algoritmos
* Aplicar Feature Engineering
* Comparar métricas de desempenho
* Criar dashboards para visualização dos resultados

## Autor

Erick Vieira

Graduando em Inteligência Artificial e Machine Learning, com foco em Ciência de Dados, Machine Learning e Engenharia de IA.
