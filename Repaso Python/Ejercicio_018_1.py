personas = int(input("¿Cuántas personas hay en tu grupo para cenar? ")).strip()
if personas > 8:
    print("Van a tener que esperar por una mesa.")
else:
    print("Su mesa está lista.")