import matplotlib.pyplot as plt
import numpy as np

def h(x):
    return x**5 - 2*(x**4) + 2

def dh(x):
    return 5*(x**4) - 8*(x**3)

def gradient_descent(derivative_func, initial_guess, taxa_de_aprendizado = 0.02, precisao = 0.001, max_passos = 300):
    
    x_novo = initial_guess

    lista_x = []
    lista_inc = []

    for i in range(max_passos):
        x_anterior = x_novo
        gradiente = derivative_func(x_anterior)
        x_novo = x_anterior - gradiente * taxa_de_aprendizado
        lista_x.append(x_novo)
        lista_inc.append(derivative_func(x_novo))

        if(abs(x_anterior - x_novo) < precisao):

            break

    return x_novo, lista_x, lista_inc

x = np.linspace(start = -2.5, stop = 2.5, num = 1000)

minimo_local, lista_x, lista_deriv = gradient_descent(derivative_func = dh,initial_guess=0.2)
print("Valor minimo local:", minimo_local)
print("Custo do valor minimo:", h(minimo_local))
print("Passos dados:", len(lista_x))




plt.figure(figsize=([15,5]))

plt.subplot(1, 2, 1)
plt.title("Função de custo")
plt.xlim(-1.2, 2.5)
plt.ylim(-1, 4)

plt.xlabel("x")
plt.ylabel("h(x)")


plt.plot(x, h(x), color = "blue", linewidth = 5, alpha = 0.8)
plt.scatter(lista_x, h(np.array(lista_x)), color = "red", s = 100, alpha = 0.6)




plt.subplot(1, 2, 2)
plt.title("Derivada da funçao de custo")
plt.xlim(-1, 2)
plt.ylim(-4, 5)
plt.grid("True")

plt.xlabel("x")
plt.ylabel("dg(x)")

plt.plot(x, dh(x), color = "skyblue", linewidth = 5, alpha = 0.8)
plt.scatter(lista_x, lista_deriv, color = "red", s = 100, alpha = 0.6)



plt.show()