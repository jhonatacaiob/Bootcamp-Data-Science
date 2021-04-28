import pandas as pd
from pandas import DataFrame as df
import matplotlib.pyplot as plt


#Lendo o arquivo
dados = pd.read_csv("lsd_math_score_data.csv")


time = dados[["Time_Delay_in_Minutes"]]
LSD = dados[["LSD_ppm"]]
score = dados[["Avg_Math_Test_Score"]]




plt.plot(time, LSD, c = "red", linewidth = 4)

plt.xlim(0, 500)
plt.ylim(1,7)
plt.title("Concentração de LSD no tecido ao longo do tempo", fontsize=17)
plt.xlabel("Tempo em minutos", fontsize=14)
plt.ylabel("Concentraçao de LSD", fontsize=14)
plt.text(x=0, y= 0.3, s="Wagner et al. (1968)", fontsize=10)

plt.savefig("Concentração de LSD no tecido ao longo do tempo.jpg")
