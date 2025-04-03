from user import User

class Privilegios:
    def __init__(self, privilegios):
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        print("Privilegios del administrador:")
        for privilegio in self.privilegios:
            print(f"- {privilegio}")


class Admin(User):
    def __init__(self, nombre, apellido, edad, email, pais, privilegios):
        super().__init__(nombre, apellido, edad, email, pais)
        self.privilegios_obj = Privilegios(privilegios)

    def mostrar_privilegios(self):
        self.privilegios_obj.mostrar_privilegios()