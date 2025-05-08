from pathlib import Path
import json

def obtener_datos_guardados(path):
    """Intenta recuperar los datos guardados de la persona."""
    if path.exists():
        contenido = path.read_text()
        datos = json.loads(contenido)
        return datos
    else:
        return None

def obtener_nuevos_datos(path):
    """Pide nuevos datos a la persona y los guarda."""
    nombre = input("¿Cómo te llamás? : ").strip().capitalize()
    edad = input("¿Cuántos años tenés? : ").strip()
    ciudad = input("¿En qué ciudad vivís? : ").strip().capitalize()

    datos = {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad
    }

    contenido = json.dumps(datos)
    path.write_text(contenido)
    return datos

def saludar_persona():
    """Saluda y muestra lo que recuerda sobre la persona."""
    path = Path("persona.json")
    datos = obtener_datos_guardados(path)
    
    if datos:
        print(f"¡Hola de nuevo, {datos['nombre']}!")
        print(f"Recordamos que tenés {datos['edad']} años y vivís en {datos['ciudad']}.")
    else:
        datos = obtener_nuevos_datos(path)
        print(f"¡Te vamos a recordar cuando vuelvas, {datos['nombre']}!")

saludar_persona()
