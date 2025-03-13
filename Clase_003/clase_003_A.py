nombre = input("Tu nombre pa: ").capitalize()  # Devuelve una copia con la primera letra en mayúscula
print("Buenos días", nombre)
print("Tu nombre sin vocales es:", nombre.strip('aeiouAEIOU.')) # Usamos .strip() para eliminar las solamente las vocales de nombre