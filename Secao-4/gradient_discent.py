import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2 + x + 1

def df(x):
    return 2*x + 1


x = np.linspace(start = -3, stop = 3, num = 500)



x_novo = 3
x_anterior = 0
taxa_de_aprendizado = 0.1
precisao = 0.00001


x_novos = []

for i in range(50000):
    x_anterior = x_novo
    gradiente = df(x_anterior)
    x_novo = x_anterior - gradiente * taxa_de_aprendizado
    if(abs(x_anterior - x_novo) < precisao):
        print("Numero de tentativas:", i)
        break

    
    x_novos.append(x_novo)


print("Valor minimo:", x_novo)
print("Inclinaçao, ou o valor de df(x) neste ponto:", df(x_novo))
print("Custo neste ponto:", f(x_novo))

x_novos = np.array(x_novos)









plt.figure(figsize=[15,5])


plt.subplot(1,2,1)
plt.title("Função de custo")
plt.xlim(-3, 3)
plt.ylim(0, 8)

plt.xlabel("x")
plt.ylabel("f(x)")


plt.plot(x, f(x), color = "blue", linewidth = 5, alpha = 0.8)
plt.scatter(x_novos, f(x_novos), color = "red", s = 100, alpha = 0.6)




plt.subplot(1,2,2)
plt.title("Derivada da funçao de custo")
plt.xlim(-2, 3)
plt.ylim(-3, 6)
plt.grid("True")

plt.xlabel("x")
plt.ylabel("df(x)")

plt.plot(x, df(x), color = "skyblue", linewidth = 5, alpha = 0.8)
plt.scatter(x_novos, df(x_novos), color = "red", s = 100, alpha = 0.6)




plt.show()
#plt.savefig("Aula 04.jpg")