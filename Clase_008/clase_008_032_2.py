# Aseguramos que el archivo 'learning_python.txt' está en el mismo directorio.
file_path = 'learning_python.txt'

# Leyendo todo el archivo de una sola vez y mostrando en pantalla
with open(file_path, 'r') as file:
    content = file.read()  # Lee todo el contenido del archivo
    print("Contenido leído todo de una vez:")
    print(content)

# Almacenando las líneas en una lista y recorriéndolas con un bucle
with open(file_path, 'r') as file:
    lines = file.readlines()  # Lee todas las líneas y las guarda en una lista

print("\nContenido leído línea por línea:")
for line in lines:
    print(line.strip())  # Imprime cada línea sin los saltos de línea adicionales
