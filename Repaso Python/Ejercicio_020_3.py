respuestas = []
numero_de_usuarios = int(input("¿Cuántas personas van a responder la encuesta? "))
for i in range(numero_de_usuarios):
    respuesta = input("Si pudieras visitar un lugar en el mundo, ¿a dónde irías? ")
    respuestas.append(respuesta)
print("\nResultados de la encuesta sobre destinos de vacaciones soñados:")
for i, respuesta in enumerate(respuestas, 1):
    print(f"Persona {i}: {respuesta}")
