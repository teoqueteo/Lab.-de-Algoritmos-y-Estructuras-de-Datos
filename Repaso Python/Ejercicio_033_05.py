def mostrar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            print(f"\nContenido de {nombre_archivo}:")
            print(archivo.read())
    except FileNotFoundError:
        print(f"Lo siento, no se encontró el archivo '{nombre_archivo}'.")

mostrar_archivo("gatos.txt")
mostrar_archivo("perros.txt")