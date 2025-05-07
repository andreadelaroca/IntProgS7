import datetime as dt
import time
import os

fecha = dt.date.today()
print(f"Fecha actual: {fecha}")

cant = int(input("Cuantas notas: "))

suma = 0
for i in range(cant):
    nota = int(input(f"Ingresa la calificación {i + 1}: "))
    suma += nota
    
promedio = suma / cant
cont = 0
tiempo_espera = 1
max_pasos = 10
espacios_iniciales = 10
os.system("cls || clear")

while cont < max_pasos:
    puntos = "." * (cont + 1)
    espacios = " " * (espacios_iniciales - cont)
    porcentaje = f"{(cont + 1) * 10}%"
    print(f"Calculando promedio{puntos}{espacios}{porcentaje}")
    time.sleep(tiempo_espera)
    cont += 1
    
print(f"El promedio es: {round(promedio, 1)}")
