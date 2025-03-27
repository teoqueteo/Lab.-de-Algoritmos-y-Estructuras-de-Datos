lenguajes_favoritos = {'Juan': 'python', 'Sara': 'c', 'Eduardo': 'rust', 'Agustina': 'c#'}
personas_a_encuestar = ['Juan', 'Sara', 'Eduardo', 'Agustina', 'Carlos', 'Marta', 'Luis']
for persona in personas_a_encuestar:
    if persona in lenguajes_favoritos:
        print(f"Gracias {persona}, ya respondiste la encuesta.")
    else:
        print(f"Hola {persona}, por favor, participa en la encuesta sobre lenguajes favoritos.")