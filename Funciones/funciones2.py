"""
Funciones en Python
Argumentos indeterminados
Estos nos sirven en el caso de que no sepamos cuantos elementos enviaremos a una funcion, para esto usamos los parametros indeterminados por posicion y por nombre.

Por posicion
Si queremos recibir un  numero indeterminado de parametros por posicion, se tiene que crear una lista dinamica de argumentos(es una tupla), definimos el parametro con un asterisco *

def indeterminado_posicion(*args):
    for i in args:
        print(i)
indeterminado_posicion(5, "Daniel", [1,2,3,'c'])   

Por nombre
Para recibir un numero no determinado de parametro por nombre(clave:valor (Keyword args)), se debe crear un diccionario dinamico de argumentos definiendo el parametro con 2 asteriscos.

def indeterminados_nombre(**kwargs):
    print(kwargs)

indeterminados_nombre(n=5, c="Hola", l=[1,2,3,4,5]) 
#Al recibirlo como un diccionario, puedo iterarlo y mostrar la clave y valor de cada argumento
def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])

indeterminados_nombre(n=5, c="Hola", l=[1,2,3,4,5]) 

Por posicion y nombre
Por si queremos aceptar ambos tipos de parametros al mismo tiempo, se tienen que crear ambas colecciones dinamicas. Primero los argumentos indeterminados por valor y luego los que son clave:valor

def super_funcion(*args,**kwargs):
    total = 0
    for arg in args:
        total += arg
    print("sumatorio => ", total)
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])

super_funcion(10, 50, -1, 1.56, 10, 20, 300, nombre="Hector", edad=27)

***
Los args y kwargs no son obligatorios, pero se usan por convencion.
Se usan en muchos frameworks y librerias, es una buena practica definirlos para las funciones.
***

"""

def indeterminado_posicion(*args):
    for i in args:
        print(i)
indeterminado_posicion(5, "Daniel", [1,2,3,'c'])  


def indeterminados_nombre(**kwargs):
    print(kwargs)

indeterminados_nombre(n=5, c="Hola", l=[1,2,3,4,5]) 
def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])

indeterminados_nombre(n=5, c="Hola", l=[1,2,3,4,5]) 

def super_funcion(*args,**kwargs):
    total = 0
    for arg in args:
        total += arg
    print("sumatorio => ", total)
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])

super_funcion(10, 50, -1, 1.56, 10, 20, 300, nombre="Hector", edad=27)