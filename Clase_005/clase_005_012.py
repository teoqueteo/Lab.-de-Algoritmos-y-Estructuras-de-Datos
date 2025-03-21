pizzas = ['Clásica', 'Napolitana', 'Salmón']
for pizza in pizzas:
     print(f"{pizza} es un tipo de pizza. \n")
print(((
"La pizza es, sin lugar a dudas, una de mis comidas favoritas. \n"
"No importa la variedad, siempre la disfruto al máximo, pero tengo una debilidad especial por ciertas opciones. \n"
"La pizza de salmón, con su toque suave y delicado, combinada con queso crema o incluso un poco de eneldo. \n"
"Por otro lado, la pizza clásica, con su salsa de tomate, queso fundido y una buena capa de ingredientes frescos, nunca falla. \n"
"Pero si hay una que realmente me roba el corazón es la napolitana. \n"
"La pizza es de lo mejor. \n"
)))

pizzas_amigo = pizzas[:]
pizzas.append('De cancha')
pizzas_amigo.append('De piña')
for pizza in pizzas:
     print(f"Mis pizzas favoritas son: {pizza}. \n")
for pizza in pizzas_amigo:
     print(f"Las pizzas favoritas de mi amigo/a son: {pizza}. \n")