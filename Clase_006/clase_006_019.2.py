while True:
    edad = int(input("¿Cuántos años tienes? (Escribe '0' para salir): "))
    if edad == 0:
        break
    if edad < 3:
        print("Tu entrada es gratis.")
    elif 3 <= edad <= 12:
        print("La entrada cuesta $10.")
    else:
        print("La entrada cuesta $15.")