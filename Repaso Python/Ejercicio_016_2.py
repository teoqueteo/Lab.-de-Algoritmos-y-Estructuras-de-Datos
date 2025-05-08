rios = {'Nilo': 'Egipto','Amazonas': 'Brasil','Yangtsé': 'China'}
for rio, pais in rios.items():
    print(f"El {rio} pasa por {pais}.")
print("\nRíos:")
for rio in rios.keys():
    print(rio)
print("\nPaíses:")
for pais in rios.values():
    print(pais)