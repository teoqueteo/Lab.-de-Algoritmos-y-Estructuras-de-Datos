from usuario import Administrador
admin = Administrador(
    nombre="Carlos",
    apellido="Perez",
    edad=35,
    email="carlos.perez@correo.com",
    pais="Argentina",
    privilegios=["puede agregar publicaciones", "puede eliminar publicaciones", "puede bloquear usuarios", "puede ver estadísticas"]
)
admin.mostrar_privilegios()