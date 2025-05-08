class Bateria:
    def __init__(self, capacidad_bateria=40):
        self.capacidad_bateria = capacidad_bateria

    def describir_bateria(self):
        print(f"Este auto tiene una batería de {self.capacidad_bateria} kWh.")

    def obtener_autonomia(self):
        if self.capacidad_bateria == 40:
            rango = 150
        elif self.capacidad_bateria == 65:
            rango = 225
        print(f"Este auto tiene una autonomía de {rango} kilómetros.")

    def actualizar_bateria(self):
        """Este método actualiza la batería a 65 kWh si aún no lo está."""
        if self.capacidad_bateria != 65:
            print("Actualizando la batería a 65 kWh...")
            self.capacidad_bateria = 65


class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def obtener_nombre_descriptivo(self):
        return f"{self.marca} {self.modelo} ({self.año})"


class AutoElectrico(Auto):
    """Representa aspectos de un auto, específicos de los vehículos eléctricos."""
    def __init__(self, marca, modelo, año):
        """Inicializa los atributos de la clase padre.
        Luego inicializa los atributos específicos de un auto eléctrico.
        """
        super().__init__(marca, modelo, año)
        self.bateria = Bateria()

mi_leaf = AutoElectrico('Nissan', 'Leaf', 2024)

print(mi_leaf.obtener_nombre_descriptivo())
mi_leaf.bateria.describir_bateria()
mi_leaf.bateria.obtener_autonomia()

mi_leaf.bateria.actualizar_bateria()
mi_leaf.bateria.obtener_autonomia()