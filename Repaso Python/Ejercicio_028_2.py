class Usuario:
    def __init__(self, nombre, apellido, edad, email, pais):
        """Inicializa los atributos del usuario"""
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email
        self.pais = pais
        self.intentos_login = 0 

    def describir_usuario(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Correo electrónico: {self.email}")
        print(f"País: {self.pais}")

    def saludar_usuario(self):
        print(f"¡Hola, {self.nombre}! Bienvenido a tu perfil.")

    def incrementar_intentos_login(self):
        self.intentos_login += 1

    def reiniciar_intentos_login(self):
        self.intentos_login = 0

usuario1 = Usuario("Juan", "Pérez", 28, "juanperez@example.com", "Argentina")
usuario1.incrementar_intentos_login()
usuario1.incrementar_intentos_login()
usuario1.incrementar_intentos_login()
print(f"Intentos de login después de incrementar: {usuario1.intentos_login}")
usuario1.reiniciar_intentos_login()
print(f"Intentos de login después de reiniciar: {usuario1.intentos_login}")
