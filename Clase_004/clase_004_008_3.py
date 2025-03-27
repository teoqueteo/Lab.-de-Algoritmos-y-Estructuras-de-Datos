invitados = ['Marcelote', 'Juan Carlos', 'Esternocleidomastoideo']
for invitado in invitados:
    print(f"Hola {invitado}, te invito a cenar. ¡Espero verte!")
ausente = invitados.pop(0)
print(f"\n {ausente} no puede venir. \n")
invitados.insert(0, 'Australopithecus')
for invitado in invitados:
    print(f"Hola {invitado}, te invito a cenar. ¡Espero verte!")
print("\n Se consiguió una mesa más grande, tres personas más podrán venir. \n")
invitados.insert(0, 'Rigoberto')
invitados.insert(len(invitados) // 2, 'Susanita')
invitados.append('El Santi')
for invitado in invitados:
    print(f"Hola {invitado}, te invito a cenar. ¡Espero verte!")