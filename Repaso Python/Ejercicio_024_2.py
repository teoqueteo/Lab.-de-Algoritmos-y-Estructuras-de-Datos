mensajes = [
    "¡Hola, ¿cómo estás?",
    "¡Hoy es un gran día para faltar!",
    "No olvides tu cita a las 3 am con el Coco.",
    "Te busca el FBI por altos niveles de facha.",
    "Esternocleidomastoideo"]
mensajes_enviados = []

def enviar_mensajes():
    while mensajes:
        mensaje = mensajes.pop(0)
        print(mensaje)
        mensajes_enviados.append(mensaje)
enviar_mensajes()
print("\nMensajes pendientes:", mensajes)
print("Mensajes enviados:", mensajes_enviados)
