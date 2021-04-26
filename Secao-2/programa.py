import pandas as pd
from pandas import DataFrame as df
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Lendo o arquivo
dados = pd.read_csv("Secao-2\cost_revenue_clean.csv")


#dando atalho as colunas (desnecessário para o projeto, pode se fazer sem isso)
colunas = {"x": df(dados[dados.columns[0]]),
             "y": df(dados[dados.columns[1]])}



#Definindo os valores da regressão linear
regressao = LinearRegression()
regressao.fit(colunas["x"], colunas["y"])
predicao = regressao.predict(colunas["x"])


#criando o grafico
plt.scatter(dados[dados.columns[0]], dados[dados.columns[1]], alpha = 0.3)
plt.plot(colunas["x"], predicao, linewidth = 4, color = "red")


#formatando o grafico
plt.title("Custo do filme vs Receita global")
plt.xlabel("Custo do filme $")
plt.ylabel("Receita Global $")


#Definindo os limites como o maior valor de cada tabela
plt.xlim(0, int(colunas["x"].max()))
plt.ylim(0, int(colunas["y"].max()))

plt.show()


