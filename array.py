#array: estructura de datos que almacena elementos del mismo tipo

numero = input("Dime un número: ")

repetidos = [0] * 10
#repetidos crea una lista de 10 veces 0 como índices

for digito in numero:
    if digito.isdigit():
        repetidos[int(digito)] += 1
#isdigit asegura que sea un digito

for i in range(10):
    if repetidos[i] > 0:
        print(f"El digito {i} aparece {repetidos[i]} veces.")
#se convierte el dígito a número y se suma uno
# ej: 2, el digito 2 aparece 1 veces
#fua chaval