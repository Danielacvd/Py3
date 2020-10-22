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

Retorno:
Lo importante del return es que con el puedo sacar devolver valores, al momento de devolver valores la ejecucion de la funcion termina.
Puedo devolver multiples valores, separandolos por comas. Pero estos valores se trataran en conjunto como su fueran una tupla, inmutables, pero se pueden reasignar a otras variables.

Envio de valores
Ademas de devolver valores, puedo recibir valores
Syntax:
def nombre_funcion(a, b):
    resultado = a+b
    return resultado

nombre_funcion(a, b) #No necesariamente el nombre de la variable que entrego tiene que ser el que recibo en los parametros de la funcion.

def suma(a, b):
    return a+b

resultado = suma(5,5)
print(resultado)



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


def suma(a, b):
    return a+b

resultado = suma(5,5)
print(resultado)

