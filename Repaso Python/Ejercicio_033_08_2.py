import json
with open("numero_favorito.json", "r") as archivo:
    numero = json.load(archivo)

print(f"¡Sé cuál es tu número favorito! Es {numero}.")
