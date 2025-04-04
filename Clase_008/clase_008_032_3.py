nombre_archivo = 'learning_python.txt'

with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        linea_modificada = linea.replace('Python', 'C')
        print(linea_modificada, end='')