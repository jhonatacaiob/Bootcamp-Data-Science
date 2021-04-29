import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2 + x + 1

def df(x):
    return 2*x + 1


x_1 = np.linspace(start = -3, stop = 3, num = 500)


plt.figure(figsize=[15,5])


plt.subplot(1,2,1)
plt.title("Função de custo")
plt.xlim(-3, 3)
plt.ylim(0, 8)

plt.xlabel("x")
plt.ylabel("f(x)")

plt.plot(x_1, f(x_1), color = "blue", linewidth = 5)





plt.subplot(1,2,2)
plt.title("Derivada da funçao de custo")
plt.xlim(-2, 3)
plt.ylim(-3, 6)
plt.grid("True")

plt.xlabel("x")
plt.ylabel("df(x)")

plt.plot(x_1, df(x_1), color = "skyblue", linewidth = 5)



plt.savefig("Aula 04.jpg")