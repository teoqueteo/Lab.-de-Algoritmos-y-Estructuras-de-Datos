while True:
    try:
        num1 = int(input("Ingresá el primer número: "))
        num2 = int(input("Ingresá el segundo número: "))
        suma = num1 + num2
        print(f"La suma de {num1} y {num2} es {suma}.")
        break
    except ValueError:
        print("Error: por favor, ingresá solo números válidos.")