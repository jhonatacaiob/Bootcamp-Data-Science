import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2 + x + 1




x_1 = np.linspace(start = -3, stop = 3, num = 500)



plt.xlim(-3, 3)
plt.ylim(min(f(x_1)), max(f(x_1)))

plt.xlabel("x")
plt.ylabel("f(x)")

plt.plot(x_1, f(x_1))
plt.show()


