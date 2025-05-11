#factorial de un número
#pide al usuario un número entero positivo y cálcula su factorial
#usar while y acumulador (producto)

num = int(input("Introduce un número entero positivo: "))
producto = 1

while num > 0:
    producto *= num
    num -= 1

print(f"El factorial es: {producto}")
