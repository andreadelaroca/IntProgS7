#suma de los primeros n numeros

while True:
    n = int(input("Ingrese un número entero positivo: "))
    if n > 0:
        break
    print("Intente otra vez")

for i in range(1,n+1):
    resultado = n + i
    
    print(f"{n} + {i} = {resultado}")
