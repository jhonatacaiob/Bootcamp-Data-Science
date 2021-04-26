
import pandas as pd
from pandas import DataFrame as df
import matplotlib.pyplot as plt


dados = pd.read_csv("Secao-2\cost_revenue_clean.csv")




plt.scatter(dados[dados.columns[0]], dados[dados.columns[1]])
plt.show()


