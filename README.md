# Projeto de Machine Learning - Previsão de Salário

## Sobre o Projeto

Este projeto tem como objetivo desenvolver um modelo de Machine Learning capaz de prever salários com base em características profissionais, como anos de experiência e quantidade de cursos realizados.

O projeto foi desenvolvido para consolidar conhecimentos em Ciência de Dados, Estatística, Análise Exploratória de Dados e Machine Learning utilizando Python e Scikit-Learn.

---

## Tecnologias Utilizadas

* Python
* Pandas
* Matplotlib
* Scikit-Learn
* Jupyter Notebook

---

## Estrutura do Projeto

```text
previsao-salario-machine-learning/
│
├── dados/
│   └── salarios.csv
│
├── notebooks/
│   └── previsao_salario.ipynb
│
├── src/
│   └── modelo.py
│
├── README.md
│
└── requirements.txt
```

---

## Dataset

O conjunto de dados contém as seguintes variáveis:

| Variável    | Descrição                        |
| ----------- | -------------------------------- |
| experiencia | Anos de experiência profissional |
| cursos      | Quantidade de cursos realizados  |
| salario     | Salário mensal (variável alvo)   |

---

## Metodologia

### 1. Análise Exploratória de Dados (EDA)

Foram realizadas análises estatísticas para compreender o comportamento dos dados:

* Visualização das primeiras linhas
* Verificação de tipos de dados
* Estatísticas descritivas
* Análise de correlação

### 2. Visualização

Foi utilizado um gráfico de dispersão para analisar a relação entre experiência profissional e salário.

### 3. Preparação dos Dados

Separação entre variáveis independentes (features) e variável alvo (target).

**Features (X):**

* Experiência
* Cursos

**Target (y):**

* Salário

Divisão dos dados:

* 80% para treinamento
* 20% para teste

### 4. Treinamento do Modelo

Foi utilizado o algoritmo de Regressão Linear através da biblioteca Scikit-Learn.

```python
from sklearn.linear_model import LinearRegression
```

### 5. Avaliação do Modelo

A performance foi avaliada utilizando a métrica:

* Mean Absolute Error (MAE)

O MAE representa o erro médio absoluto entre os valores reais e os valores previstos pelo modelo.

---

## Resultados

O modelo foi capaz de identificar a relação entre experiência profissional, quantidade de cursos realizados e salário, produzindo previsões consistentes para novos registros.

---

## Conhecimentos Aplicados

* Python para análise de dados
* Manipulação de dados com Pandas
* Estatística descritiva
* Correlação entre variáveis
* Regressão Linear
* Machine Learning Supervisionado
* Avaliação de Modelos com MAE

---

## Próximos Passos

* Utilizar datasets reais e mais robustos
* Aplicar técnicas de Feature Engineering
* Comparar diferentes algoritmos de Machine Learning
* Implementar novas métricas de avaliação
* Desenvolver dashboards para análise dos resultados

---

## Autor

**Erick Vieira**

Graduando em Inteligência Artificial e Machine Learning.

Áreas de interesse:

* Ciência de Dados
* Machine Learning
* Inteligência Artificial
* Engenharia de IA
* MLOps
