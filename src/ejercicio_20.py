mayor = None

while True:
    entrada = input("Ingresa una edad (-1 para terminar): ")
    try:
        edad = int(entrada)
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    if edad == -1:
        break

    if mayor is None or edad > mayor:
        mayor = edad

if mayor is not None:
    print(f"La edad mayor ingresada es: {mayor}")
else:
    print("No se ingresaron edades válidas.")