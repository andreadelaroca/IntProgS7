#pedir una contraseña hasta que sea correcta

contraseña_correcta = "1234"
intentos = 0

while True:
    entrada = input("Ingrese la contraseña: ")
    intentos += 1
    
    if entrada == contraseña_correcta:
        print("La contraseña es válida")
        break
    else:
        print("La contraseña es inválida")

