import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-5, 5, 100)
#y = np.cosh(x)
plt.plot(x, 2*x+1,
         color="red",
         linestyle="-.",
         linewidth=2,
         label="2x+1")
plt.plot(x, x**2,
         color="green",
         linestyle="-.",
         linewidth=2,
         label="x^2")

plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("Grafica de f(x)")
plt.grid()

#plt.savefig("cose_hiperbolico.png") #para guardar como pdf solo cambiar .png a .pdf
plt.show()