usuarios_actuales = ['admin','pepe','micho','marce','eduardo']
usuarios_nuevos = ['admin','pepe','titi','gerardo','emilianio']
for usuario_nuevo in usuarios_nuevos:
    for usuario_actual in usuarios_actuales:
        if usuario_nuevo == usuario_actual:
            print(f"Nombre ya usado, elegí otro.")
        else:
            print(f"Nombre aceptado.")