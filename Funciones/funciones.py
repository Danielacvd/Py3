"""
Funciones en python3

"""

def nombre_funcion(parametro):
    return f"Hola {parametro}"

print(nombre_funcion("Daniel"))


def sin_parametro():
    n1 = 10
    n2 = 20
    print(f"Suma: {n1 + n2}")

sin_parametro()

def parametro_por_defecto(nombre = "Daniel"):
    return f"Hola {nombre}"

print(parametro_por_defecto("Feña"))