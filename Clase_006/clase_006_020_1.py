pedidos_sandwiches = ['atún', 'jamón y queso', 'pollo', 'vegetariano', 'milanesa']
sandwiches_terminados = []
for sandwich in pedidos_sandwiches:
    print(f"Preparé tu sándwich de {sandwich}.")
    sandwiches_terminados.append(sandwich)
print("\nSándwiches terminados:")
for sandwich in sandwiches_terminados:
    print(f"- {sandwich}")