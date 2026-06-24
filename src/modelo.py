import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


df = pd.read_csv("dados/salarios.csv")

X = df[["experiencia", "cursos"]]
y = df["salario"]

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

modelo = LinearRegression()

modelo.fit(X_treino, y_treino)

previsoes = modelo.predict(X_teste)

mae = mean_absolute_error(y_teste, previsoes)

print("Previsões:", previsoes)
print("Valores reais:", y_teste.values)
print("MAE:", mae)

nova_pessoa = pd.DataFrame(
    [[5, 4]],
    columns=["experiencia", "cursos"]
)

salario_previsto = modelo.predict(nova_pessoa)

print(f"Salário previsto: R$ {salario_previsto[0]:.2f}")
