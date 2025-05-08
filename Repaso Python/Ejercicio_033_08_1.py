import json
numero = input("¿Cuál es tu número favorito? Ingresalo: ")

with open("numero_favorito.json", "w") as archivo:
    json.dump(numero, archivo)
