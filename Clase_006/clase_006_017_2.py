mascota_1 = {'Animal': 'Perro', 'Nombre': 'Rex', 'Dueño': 'Carlos'}
mascota_2 = {'Animal': 'Gato', 'Nombre': 'Miau', 'Dueño': 'Laura'}
mascota_3 = {'Animal': 'Conejo', 'Nombre': 'Bunny', 'Dueño': 'Pedro'}
mascota_4 = {'Animal': 'Tortuga', 'Nombre': 'Shelly', 'Dueño': 'Sofia'}

# Guardar los diccionarios en una lista llamada mascotas
mascotas = [mascota_1, mascota_2, mascota_3, mascota_4]

# Recorrer la lista y mostrar la información de cada mascota
for mascota in mascotas:
    for info, dato in mascota.items():
        print(f"{info}: {dato}. \n")