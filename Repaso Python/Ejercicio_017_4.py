ciudades = {
    'París': {'país': 'Francia', 'población': '2.165.000', 'dato': 'La Torre Eiffel es uno de los monumentos más visitados del mundo.'},
    'Tokio': {'país': 'Japón', 'población': '37.833.000', 'dato': 'Es la ciudad con la mayor población en el mundo.'},
    'Nairobi': {'país': 'Kenia', 'población': '4.397.073', 'dato': 'Es conocida como la "ciudad verde del sol".'}}
for ciudad, info in ciudades.items():
    print(f"Ciudad: {ciudad}")
    for clave, valor in info.items():
        print(f"  {clave.capitalize()}: {valor}")