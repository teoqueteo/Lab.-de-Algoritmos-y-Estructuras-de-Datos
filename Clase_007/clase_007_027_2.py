class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        print(f"Restaurante: {self.nombre_restaurante}")
        print(f"Tipo de cocina: {self.tipo_cocina}")

    def abrir_restaurante(self):
        print(f"¡El restaurante {self.nombre_restaurante} está abierto!")

restaurante1 = Restaurante("La Casa del Sabor", "Cocina italiana")
restaurante2 = Restaurante("El Refugio del Mar", "Cocina de mariscos")
restaurante3 = Restaurante("La Parrilla del Barrio", "Cocina argentina")

print("\nDescripción del restaurante 1:")
restaurante1.describir_restaurante()

print("\nDescripción del restaurante 2:")
restaurante2.describir_restaurante()

print("\nDescripción del restaurante 3:")
restaurante3.describir_restaurante()