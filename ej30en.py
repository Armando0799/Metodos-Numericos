#$\textbf{Ejercicio}:$ Hacer una tabla con los valores $1/n, 1/n^2, 1/n^3$ y $1/n^4$ 
# para $n=5, 10, 100$ y $1000$ para verificar quien converge más rápido.
import numpy as np
import matplotlib.pyplot as plt

print("="*80)
print(f"{'n':^8} | {'1/n':^15} | {'1/n^2':^15} | {'1/n^3':^15} | {'1/n^4':^15}")
print("="*80)

for n in [5, 10, 100, 1000]:
    p = 1/n
    p_2 = 1/n**2
    p_3 = 1/n**3
    p_4 = 1/n**4

    print(f"{n:^8} | {p:^15} | {p_2:^15.8f} | {p_3:^15.11f} | {p_4:^15.13f}")

print("="*80)

x = np.linspace(1, 100, 400)

plt.figure(figsize=(12, 8))

plt.plot(x, 1/x, label="1/n", linewidth=2, color='black')
plt.plot(x, 1/x**2, label="1/n^2", linewidth=2, color='red')
plt.plot(x, 1/x**3, label="1/n^3", linewidth=2, color='blue')
plt.plot(x, 1/x**4, label="1/n^4", linewidth=2, color='green')


plt.xlabel("n")
plt.ylabel("f(n)")
plt.title("Convergencia de la secuencia 1/n^k")
plt.legend()
plt.grid()
plt.show()