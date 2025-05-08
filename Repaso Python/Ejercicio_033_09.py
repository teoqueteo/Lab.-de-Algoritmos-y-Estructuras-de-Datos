import json
import os

archivo_nombre = "numero_favorito.json"

if os.path.exists(archivo_nombre):
    with open(archivo_nombre, "r") as archivo:
        numero = json.load(archivo)
    print(f"¡Sé cuál es tu número favorito! Es {numero}.")
else:
    numero = input("¿Cuál es tu número favorito? Ingresalo: ")
    with open(archivo_nombre, "w") as archivo:
        json.dump(numero, archivo)
    print("Tu número favorito ha sido guardado.")
