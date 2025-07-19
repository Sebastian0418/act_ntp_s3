contador_palabras = 0
palabra = ""

print("Escribe palabras. Cuando quieras terminar, escribe 'fin'.")

while palabra.lower() != "fin":
    palabra = input("Escribe una palabra: ")
    if palabra.lower() != "fin":
        contador_palabras += 1

print(f"\nSe leyeron {contador_palabras} palabras en total.")