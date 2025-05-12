#suma de números pares e impares
#Calcula la suma de los números pares y la suma de los números impares
#usar while, acumladores para la suma de pares e impares

numeros = input("Ingresa una lista de números separados por espacios (utilice 0 como valor final): ")

numeros = numeros.split()
suma_pares = 0
suma_impares = 0
cont = 0

while cont < len(numeros): #len es la longitud de la lista
    if int(numeros[cont]) == 0:
        break
    if int(numeros[cont]) % 2 == 0:
        suma_pares += int(numeros[cont])
    else:
        suma_impares += int(numeros[cont])
    cont += 1
        
print(f"La suma de los números pares es: {suma_pares}")
print(f"La suma de los números impares es: {suma_impares}")
