persona_1 = {'Nombre': 'Sal', 'Apellido': 'Chicha', 'Edad': '70', 'Ciudad': 'La Paz'}
persona_2 = {'Nombre': 'Ana', 'Apellido': 'Gomez', 'Edad': '28', 'Ciudad': 'Madrid'}
persona_3 = {'Nombre': 'Luis', 'Apellido': 'Pérez', 'Edad': '34', 'Ciudad': 'Buenos Aires'}
personas = [persona_1, persona_2, persona_3]
for persona in personas:
    for info, dato in persona.items():
        print(f"{info}: {dato}. \n")