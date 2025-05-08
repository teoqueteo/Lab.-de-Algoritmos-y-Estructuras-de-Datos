import random

elementos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
my_ticket = random.sample(elementos, 4)

intentos = 0

while True:
    ganadores = random.sample(elementos, 4)
    intentos += 1
    if ganadores == my_ticket:
        print(f"Ganaste. Tu boleto ({my_ticket}) salió después de {intentos} intentos.")
        break