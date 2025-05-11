#suma de los primeros n numeros

n = int(input("Ingrese un número entero positivo: "))

for i in range(1,n):
    resultado = n + i
    print(f"{n} + {i} = {resultado}")
