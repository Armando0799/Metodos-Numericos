#funciones
#def nombre_(objetivo-s)
#codigo
#return (devuelva)

#def multi (n):
  #m=2*n
  # return m
#n=int(input("ingrese un entero"))
#m=multi(n)

#print(f"el doble de {n} es: {m}")

#Ejemplo: las calificaciones de Diego y Carlos
#son respectivamente 9,8,7 y 6; 5,4,3 y 2
#¿cual es su promedio?

def prom (lista):
    sum=0
    for i in lista:
        sum=sum+i
    return sum/len(lista)


Carlos=[9, 8, 7, 6]
Diego=[5, 4, 3, 2,]

cal_Carlos=prom(Carlos)
cal_Diego=prom(Diego)

print(f"las calificaciones de Diego y Carlos son {cal_Diego} y {cal_Carlos} respectivamente")

