import matplotlib.pyplot as plt
import numpy as np

def g(x):
    return x**4 - 4*(x**2) + 5

def dg(x):
    return 4*(x**3) - 8*x

def gradient_descent(derivative_func, initial_guess, taxa_de_aprendizado = 0.01, precisao = 0.000001):
    
    x_novo = initial_guess

    lista_x = []
    lista_inc = []

    for i in range(500):
        x_anterior = x_novo
        gradiente = derivative_func(x_anterior)
        x_novo = x_anterior - gradiente * taxa_de_aprendizado
        lista_x.append(x_novo)
        lista_inc.append(derivative_func(x_novo))

        if(abs(x_anterior - x_novo) < precisao):

            break

    return x_novo, lista_x, lista_inc

x = np.linspace(start = -2, stop = 2, num = 1000)

minimo, lista_x, lista_deriv = gradient_descent(derivative_func = dg,initial_guess=3)
print("Valor minimo local:", minimo)
print("Passos dados:", len(lista_x))


plt.subplot(1, 2, 1)
plt.title("Função de custo")
plt.xlim(-2, 2)
plt.ylim(0.5, 5.5)

plt.xlabel("x")
plt.ylabel("g(x)")


plt.plot(x, g(x), color = "blue", linewidth = 5, alpha = 0.8)
plt.scatter(lista_x, g(np.array(lista_x)), color = "red", s = 100, alpha = 0.6)




plt.subplot(1, 2, 2)
plt.title("Derivada da funçao de custo")
plt.xlim(-2, 2)
plt.ylim(-6, 8)
plt.grid("True")

plt.xlabel("x")
plt.ylabel("dg(x)")

plt.plot(x, dg(x), color = "skyblue", linewidth = 5, alpha = 0.8)
plt.scatter(lista_x, lista_deriv, color = "red", s = 100, alpha = 0.6)



plt.savefig("Aula 06.jpg")