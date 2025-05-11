#contar palabras en una frase
#usar for o método con string, y un contador

frase = str(input("Introduce una frase: "))
palabra = frase.split()
#split sirve para separar una cadena en una lista de palabras
cont = 0

for i in palabra:
    cont += 1
    
print(f"La frase tiene {cont} palabras")