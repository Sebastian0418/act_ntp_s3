import random


numero_secreto = random.randint(1, 10)
adivinanza = 0

print("¡Bienvenido al juego de adivinanza!")
print("Estoy pensando en un número entre 1 y 10.")


while adivinanza != numero_secreto:
    try:
        adivinanza = int(input("¿Cuál crees que es? "))
        if adivinanza < numero_secreto:
            print("El número es más grande. ¡Intenta de nuevo!")
        elif adivinanza > numero_secreto:
            print("El número es más pequeño. ¡Intenta de nuevo!")
    except ValueError:
        print("Eso no es un número válido. Por favor, ingresa un número entero.")

print(f"¡Felicidades! ¡Adivinaste el número! Era el {numero_secreto}.")