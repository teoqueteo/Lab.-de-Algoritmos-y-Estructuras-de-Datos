pedidos_sandwiches = ['atún', 'jamón y queso', 'pastrón', 'pastrón', 'pastrón', 'pollo', 'vegetariano', 'milanesa']
print("Lo sentimos, la sandwichería se quedó sin pastrón. \n")
while 'pastrón' in pedidos_sandwiches:
    pedidos_sandwiches.remove('pastrón')
sandwiches_terminados = []
for sandwich in pedidos_sandwiches:
    print(f"Preparé tu sándwich de {sandwich}.")
    sandwiches_terminados.append(sandwich)
print("\nSándwiches terminados:")
for sandwich in sandwiches_terminados:
    print(f"- {sandwich}")