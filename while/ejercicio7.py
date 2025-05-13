#suma de números pares e impares
#usar while, acumladores para la suma de pares e impares

numeros = input("Ingresa una lista de números separados por espacios: ")

numeros = numeros.split()
suma_pares = 0
suma_impares = 0
cont = 0

while cont < len(numeros): #mientras cont sea menor que la longitud de la lista
    numero = int(numeros[cont]) #convertir el número a entero
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero
    cont += 1
    
print(f"La suma de los números pares es: {suma_pares}")
print(f"La suma de los números impares es: {suma_impares}")
