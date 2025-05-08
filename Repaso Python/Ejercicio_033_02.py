print("Ingresá los nombres de los invitados. Escribí 'salir' para terminar.")
with open("guest_book.txt", "w") as archivo:
    while True:
        nombre = input("Nombre: ").strip().capitalize()
        if nombre.lower() == "salir":
            break
        archivo.write(nombre + "\n")
        print(f"¡Bienvenido, {nombre}!")
print("Todos los nombres han sido guardados en guest_book.txt.")