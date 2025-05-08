def obtener_pi():
    with open("1M_pi.txt", "r") as archivo:
        pi = archivo.read().strip()
    return pi

def verificar_fecha(fecha, pi):
    if fecha in pi:
        return f"¡Sí! La fecha {fecha} aparece en los primeros un millón de dígitos de Pi."
    else:
        return f"Lo siento, la fecha {fecha} no aparece en los primeros un millón de dígitos de Pi."

def main():
    pi = obtener_pi()
    fecha_nacimiento = input("Introduce tu fecha de nacimiento (formato sin guiones, ej. 12121834): ")
    resultado = verificar_fecha(fecha_nacimiento, pi)
    print(resultado)

if __name__ == "__main__":
    main()
