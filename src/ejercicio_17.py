while True:
    try:
        numero_str = input("Por favor, ingresa un número entero positivo: ")
        
        numero_int = int(numero_str)

        if numero_int < 0:
            print("El número debe ser positivo. Inténtalo de nuevo.")
        else:
            suma_digitos = 0
           
            for digito_char in numero_str:
                suma_digitos += int(digito_char) 

            print(f"La suma de los dígitos de {numero_str} es: {suma_digitos}")
            break 
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")