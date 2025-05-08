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
print("\n Se pueden invitar solo a dos personas. \n")
n_lista = len(invitados)
while n_lista != 2:
    desinvitado = invitados.pop()
    print(f"Lo siento {desinvitado}, te desinvito.")
    n_lista = len(invitados)
print("\n")
for invitado in invitados:
    print(f"Hola {invitado}, sigues invitado a la cena.")
del invitados[-2:]
print(f"\n {invitados}")