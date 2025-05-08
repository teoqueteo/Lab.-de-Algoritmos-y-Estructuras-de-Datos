class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        print(f"Restaurante: {self.nombre_restaurante}")
        print(f"Tipo de cocina: {self.tipo_cocina}")

    def abrir_restaurante(self):
        print(f"¡El restaurante {self.nombre_restaurante} está abierto!")

class PuestoDeHelados(Restaurante):
    def __init__(self, nombre, direccion, sabores):
        super().__init__(nombre, "Heladería")
        self.direccion = direccion
        self.sabores = sabores
    def mostrar_sabores(self):
        print("Sabores disponibles:")
        for sabor in self.sabores:
            print(f"- {sabor}")
puestos_helados = PuestoDeHelados("Helados del Mar", "Calle del Sol 123", ["Vainilla", "Chocolate", "Fresa", "Menta"])
puestos_helados.mostrar_sabores()