"""
Funciones en python3

Definicion o llamada:
Syntax Basica:
def nombre_funcion():
    codigo....
    return codigo

#llamo desde el cuerpo del programa

nombre_funcion()    


Dentro de la funcion puedo declarar variables, inicializarlas, etc
Pero para que estan variables puedan vivir fuera de la funcion, las tengo que retornar
Las variables solo viven dentro de la funcion, si declaro una variable dentro de una funcion y la llamo desde fuera de la funcion dara un error, por eso se escapan o retornan usando el return o print.


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