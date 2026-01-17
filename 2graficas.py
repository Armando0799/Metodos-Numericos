import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-5, 5, 100)
plt.plot(x, x**2, label="x^2")
plt.plot(x, x**3, label="x^3")

plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("Grafica de f(x)=x²")
plt.grid()
plt.show()