try:
    num1 = int(input("Ingresá el primer número: "))
    num2 = int(input("Ingresá el segundo número: "))
    suma = num1 + num2
    print(f"La suma de {num1} y {num2} es {suma}.")
except ValueError:
    print("Por favor, ingresá solo números válidos. Intentalo de nuevo.")