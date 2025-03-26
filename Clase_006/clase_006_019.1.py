while True:
    ingrediente = input("Ingresa un ingrediente para la pizza (o escribe 'salir' para terminar): ").lower().strip()
    if ingrediente == 'salir':
        break
    print(f"Vas a agregar {ingrediente} a tu pizza.") 