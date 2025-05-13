#Simulación de un cajero automático (simplificado)
#Simula un cajero automático con un saldo inicial.
# Permite al usuario realizar depósitos (sumar al saldo) y retiros (restar del saldo) 
# hasta que decida salir. Muestra el saldo actual en cada operación.

saldo_inicial = 1000.0
saldo = saldo_inicial

print("Bienvenido al cajero automático")
print(f"Su saldo actual es ${saldo}")
while True:
    print("\nSelecciona una opción:")
    print("1 - Realizar depósito")
    print("2 - Retirar efectivo")
    print("3 - Salir")
    opcion = int(input("Digite su opción: "))
    if opcion == 1:
        deposito = float(input("Ingrese la cantidad a depositar: $"))
        saldo += deposito
        print(f"Depósito exitoso. Su saldo actual es ${saldo}")
    elif opcion == 2:
        retiro = float(input("Ingrese la cantidad a retirar: $"))
        if retiro > saldo:
             print("Fondos insuficientes.")
        else:
            saldo -= retiro
            print(f"Retiro exitoso. Su saldo actual es ${saldo}")
    elif opcion == 3:
        print("Gracias por preferirnos, vuelva pronto.")
        break