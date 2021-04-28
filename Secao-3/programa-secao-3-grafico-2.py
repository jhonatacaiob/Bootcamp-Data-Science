import pandas as pd
from pandas import DataFrame as df
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


#Lendo o arquivo
dados = pd.read_csv("lsd_math_score_data.csv")


time = dados[["Time_Delay_in_Minutes"]]
LSD = dados[["LSD_ppm"]]
score = dados[["Avg_Math_Test_Score"]]

regr = LinearRegression()

regr.fit(LSD, score)


plt.scatter(LSD, score, c = "b", s= 100, alpha = 0.7)
plt.plot(LSD, regr.predict(LSD), c = "r", linewidth = 3)


plt.grid(True)
plt.xlim(1, 6.5)
plt.ylim(25,85)
plt.title("Performance vs LSD", fontsize=17)
plt.xlabel("Concentração de LSD", fontsize=14)
plt.ylabel("Performance", fontsize=14)



plt.savefig("Performance vs LSD.jpg")  