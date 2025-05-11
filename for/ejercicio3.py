#contar vocales en una cadena
#for para la cadena y contador para cada vocal
import time
cadena = input("Escribe una cadena: ")

a = 0
e = 0
i = 0
o = 0
u = 0

for letra in cadena.lower():
    if letra == "a":
        a += 1
    elif letra == "e":
        e += 1
    elif letra == "i":
        i += 1
    elif letra == "o":
        o += 1
    elif letra == "u":
        u += 1

vocales_total = a + e + i + o + u
tiempo_espera = 2.5

print("\nContando vocales...")
time.sleep(tiempo_espera)

print(f"\nCantidad total de vocales: {vocales_total}")
print(f"Cantidad de a: {a}")
print(f"Cantidad de e: {e}")
print(f"Cantidad de i: {i}")
print(f"Cantidad de o: {o}")
print(f"Cantidad de u: {u}")
