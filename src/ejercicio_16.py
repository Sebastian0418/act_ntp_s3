import time

segundos = 0

print("Reloj Digital (00:00 - 00:59)")

while segundos <= 59:
   
    minutos_str = "00"
    segundos_str = f"{segundos:02d}" 

    print(f"{minutos_str}:{segundos_str}")
    time.sleep(1)
    segundos += 1

print("Fin del reloj.")