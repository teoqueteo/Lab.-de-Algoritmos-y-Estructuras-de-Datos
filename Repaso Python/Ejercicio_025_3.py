def hacer_auto(fabricante, modelo, **info_auto):
    info_auto['fabricante'] = fabricante
    info_auto['modelo'] = modelo
    return info_auto
auto = hacer_auto('toyota', 'corolla', color='gris', airbags=True)
for dato, info in auto.items():
    print(f"- {dato.capitalize()}: {info}")