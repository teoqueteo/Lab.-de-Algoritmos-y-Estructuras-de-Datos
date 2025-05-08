class Usuario:
    def __init__(self, nombre, apellido, edad, email, pais):
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


class Administrador(Usuario):
    def __init__(self, nombre, apellido, edad, email, pais, privilegios):
        super().__init__(nombre, apellido, edad, email, pais)
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        print(f"Privilegios del administrador {self.nombre}:")
        for privilegio in self.privilegios:
            print(f"- {privilegio}")


admin = Administrador(
    nombre="Carlos",
    apellido="Perez",
    edad=35,
    email="carlos.perez@correo.com",
    pais="Argentina",
    privilegios=["puede agregar publicaciones", "puede eliminar publicaciones", "puede bloquear usuarios", "puede ver estadísticas"]
)
admin.mostrar_privilegios()
