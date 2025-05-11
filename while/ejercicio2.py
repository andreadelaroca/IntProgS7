#producto de los primeros m números pares
#usar cont, while y acumulador
#acumulador para el producto
#contador para los pares

m = int(input("Ingrese un número entero positivo: "))

contador = 0
par = 2
producto = 1

while contador < m:
    producto *= par
    par += 2 
    contador += 1 
    
print(f"El producto de los primeros {m} números pares es: {producto}")
