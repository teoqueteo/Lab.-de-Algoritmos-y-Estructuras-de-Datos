def construir_perfil(nombre, apellido, **info_usuario):
    """Construye un diccionario con todo lo que sabemos sobre un usuario."""
    info_usuario['nombre'] = nombre
    info_usuario['apellido'] = apellido
    return info_usuario
perfil = construir_perfil('Teo', 'Echikouski',
                                   tipo='El mejor',
                                   especialidad='Ser fachero',
                                   disponibilidad='24/7')
for dato, info in perfil.items():
    print(f"- {dato.capitalize()}: {info.capitalize()}")