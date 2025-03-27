def hacer_album(artista, titulo, canciones=None):
    album = {'artista': artista, 'titulo': titulo}
    if canciones:
        album['canciones'] = canciones
    return album
print("Introduce 'salir' en cualquier momento para finalizar.")
while True:
    artista = input("Nombre del artista: ").lower().strip()
    if artista == 'salir':
        break

    titulo = input("Título del álbum: ").lower().strip()
    if titulo == 'salir':
        break

    canciones = input("Número de canciones (presiona Enter para omitir): ").lower().strip()
    if canciones == 'salir':
        break
    elif canciones.isdigit():
        canciones = int(canciones)
    else:
        canciones = None
    album = hacer_album(artista, titulo, canciones)
    print(f"Álbum creado: {album}\n")