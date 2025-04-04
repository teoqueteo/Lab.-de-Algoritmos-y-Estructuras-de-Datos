nombre_archivo = 'learning_python.txt'

with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
    contenido_completo = archivo.read()
    print("Contenido completo del archivo:\n")
    print(contenido_completo)

with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()

print("\nContenido del archivo línea por línea:\n")
for linea in lineas:
    print(linea, end='')