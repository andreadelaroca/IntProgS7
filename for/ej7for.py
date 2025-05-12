#ejercicio 7 de la guía didáctica resuelto con for
#suma de números pares e impares

numeros = input("Ingresa una lista de números separados por espacios: ")

numeros = numeros.split()
suma_pares = 0
suma_impares = 0

for suma in numeros:
    if int(suma) % 2 == 0:
        suma_pares += int(suma)
    else:
        suma_impares += int(suma)
        
print(f"La suma de los números pares es: {suma_pares}")
print(f"La suma de los números impares es: {suma_impares}")