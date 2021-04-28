import pandas as pd
from pandas import DataFrame as df
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Lendo o arquivo
dados = pd.read_csv("cost_revenue_clean.csv")


#dando atalho as colunas (desnecessário para o projeto, pode se fazer sem isso)
colunas = {"X": df(dados[dados.columns[0]]),
             "y": df(dados[dados.columns[1]])}



#Definindo os valores da regressão linear
regressao = LinearRegression()
regressao.fit(colunas["X"], colunas["y"])
predicao = regressao.predict(colunas["X"])


#criando o grafico
plt.scatter(dados[dados.columns[0]], dados[dados.columns[1]], alpha = 0.3)
plt.plot(colunas["X"], predicao, linewidth = 4, color = "red")


#formatando o grafico
plt.title("Custo do filme vs Receita global")
plt.xlabel("Custo do filme $")
plt.ylabel("Receita Global $")


#Definindo os limites do grafico
plt.xlim(0, 4.5 * (10**8))
plt.ylim(0, (3 * (10**9)))



plt.savefig("Custo do filme vs Receita global.jpg")




