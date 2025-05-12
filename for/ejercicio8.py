# Encontrar el mayor y el menor de N números
# Pide al usuario la cantidad N de números y luego solicita cada número.
# Encuentra el número mayor y el número menor.
# Usa un bucle for, y acumuladores.

mayor = None
menor = None

n = int(input("¿Cuántos números va a ingresar? "))

for i in range(n):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    if mayor is None or menor is None:
        mayor = numero
        menor = numero
    else:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
            
print(f"El número mayor es {mayor}")
print(f"El número menor es {menor}")
