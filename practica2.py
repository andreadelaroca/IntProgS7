#imprimir cada letra de una palabra

print("".join(letra.upper() if letra.lower() in "aeiou" else letra for letra in "python"))
