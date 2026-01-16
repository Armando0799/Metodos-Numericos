import math
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
#y = np.cos(x)
#a = np.exp(-x)
#b = x**3

plt.plot(x, np.cos(x),
         color="red",
         linestyle=":",
         label="cos(x)")

plt.plot(x, np.exp(-x),
         color="black",
         linestyle="-.",
         linewidth=1,
         label="exp(-x)")

plt.plot(x, x**3,
         color="blue",
         linestyle="--",
         linewidth=1,
         label="x^3")

plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("Grafica de f(x)")
plt.grid()
plt.show()