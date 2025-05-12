#calcular la frecuencia de cada digito en un número
# Usa un bucle while y un array/list de contadores (uno para cada dígito).

num = int(input("Ingrese un número entero positivo: "))
frecuencia = [0] * 10

while num > 0:
    digito = num % 10
    frecuencia[digito] += 1
    num //= 10

print("Frecuencia de cada dígito:")
for i in range(10):
    print(f"Dígito {i}: {frecuencia[i]} veces")
