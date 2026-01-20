import math
import matplotlib.pyplot as plt

x=0.5
valor_exacto = math.exp(x)
sum = 0
n_valores = []
error_relativo = []
print("="*60)
print(f"{'n':^10} | {'Aprox e^x':^14} | {'Error abs':^14} | {'Erro real':^14}")
print("="*60)

sum = 0
for n in range(20):
    sum = sum+x**n/math.factorial(n)
    erro_abs = abs(valor_exacto-sum)
    error_real=erro_abs/valor_exacto
    
    n_valores.append(n)
    error_relativo.append(error_real)
    print(f"{n:^10} | {sum:^14.8f} | {erro_abs:^14.8f} | {error_real:^14.8f}")
    
    if error_real<0.005:
        break

print("="*60)
plt.figure()
plt.plot(n_valores, error_relativo, marker='o')
plt.xlabel("n (grado del polinomio)")
plt.ylabel("error relativo")
plt.title("convergencia de la serie de taylor e^x en 0.5")
plt.show()