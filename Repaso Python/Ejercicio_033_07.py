def contar_palabra(nombre_archivo, palabra):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().lower()
            total = contenido.count(palabra)
            print(f"La palabra '{palabra}' aparece {total} veces en {nombre_archivo}.")
    except FileNotFoundError:
        print(f"No se encontró el archivo '{nombre_archivo}'.")

archivo = "The red feathers.txt"

contar_palabra(archivo, "the")
contar_palabra(archivo, "the ")
