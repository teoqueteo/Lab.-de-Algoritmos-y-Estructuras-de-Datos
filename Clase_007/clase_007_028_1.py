class Usuario:
    def __init__(self, nombre, apellido, edad, email, pais):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email
        self.pais = pais

    def describir_usuario(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Correo electrónico: {self.email}")
        print(f"País: {self.pais}")

    def saludar_usuario(self):
        print(f"¡Hola, {self.nombre}! Bienvenido a tu perfil.")

usuario1 = Usuario("Juan", "Pérez", 28, "juanperez@example.com", "Argentina")
usuario2 = Usuario("Ana", "Gómez", 34, "anagomez@example.com", "España")
usuario3 = Usuario("Carlos", "Sánchez", 25, "carlossanchez@example.com", "México")

print("\nResumen del usuario 1:")
usuario1.describir_usuario()
usuario1.saludar_usuario()

print("\nResumen del usuario 2:")
usuario2.describir_usuario()
usuario2.saludar_usuario()

print("\nResumen del usuario 3:")
usuario3.describir_usuario()
usuario3.saludar_usuario()