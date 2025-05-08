nombre = input("Por favor, ingresá tu nombre: ").strip().capitalize()
with open("guest.txt", "w") as archivo:
    archivo.write(nombre)
print(f"Hola, {nombre}. Tu nombre ha sido guardado en guest.txt.")
