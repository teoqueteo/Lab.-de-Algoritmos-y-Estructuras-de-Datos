def hacer_sandwich(*ingredientes):
    print("\nEstás pidiendo un sándwich con los siguientes ingredientes:")
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")
hacer_sandwich('jamón', 'queso', 'lechuga', 'tomate')
hacer_sandwich('pollo', 'aguacate', 'mayonesa')
hacer_sandwich('atun', 'cebolla', 'pepino', 'aceitunas', 'pimientos')
