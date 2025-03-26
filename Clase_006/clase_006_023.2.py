def hacer_album(artista, titulo, canciones=None):
    album = {'artista': artista, 'titulo': titulo}
    if canciones:
        album['canciones'] = canciones
    return album
album1 = hacer_album('Pink Floyd', 'The Dark Side of the Moon')
album2 = hacer_album('The Beatles', 'Abbey Road')
album3 = hacer_album('Nirvana', 'Nevermind')
print(album1)
print(album2)
print(album3)
album4 = hacer_album('Metallica', 'Master of Puppets', canciones=8)
print(album4)