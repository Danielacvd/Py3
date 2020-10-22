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

Arqumentos y parametros
Los valores que recibo en la funcion, se llaman parametros, pero cuando yo estoy enviando datos a una funcion, estos se llaman argumentos
Argumentos por posicion
Cuando envio un argumento, estos son recibidos por la funcion que yo estoy llamando, y se reciben por orden en los parametros recibidos.
def suma(a, b):
    return a+b
resultado = suma(5,7) # 5 seria tomara el primer lugar de los parametros, 7 el segundo (a = 5, b = 7)
Sin embargo, puede evadir este orden, si al momento de llamar la funcion y enviar los argumentos a estos les asigno el nombre del parametro
resta(b=30, a=10)
Tambien esta la llamada sin argumentos
Si llamamos a un funcion que tiene definidos parametros y al llamarla no le entregamos los argumentos necesarios, dara un error.
def suma(a,b):
    return a+b
suma()#Error
La funcion suma estara esperando que entreguemos argumentos para los parametros a y b.
Para lidiar con estos, podemos usar parametros por defecto.
def resta(a=None, b=None):
    if a == None or b == None:
        print("Faltaron los numeros para la ejecucion de la funcione")
        return
    return a-b #En caso de que lleguen los 2 argumentos realizo la operacion.
resta()

Paso por valor y referencia
Depende del tipo de dato que enviamos a la funcion, podemos diferenciar 2 comportamientos:
- Paso por valor: Se crea una copia local de la variable dentro de la funcion.
- Paso por referencia: Se maneja directamente la variable, lo cambios realizados dentro de la funcicon la afectara tambien afuera de esta.

- Los tipos simples se pasan por valor: Enteros, flotantes, cadenas, logicos(int, float, str, bool)
- Los tipos compuestos se pasan por referencia: Listas, diccionarios, conjuntos(list, dicc, set)

Paso por valor
Los numeros se pasan por valor, crean una copia dentro de la funcion, por lo que no les afecta lo que se haga con ellos dentro de una funcion

def doble(numero):
    numero *= 2
    return numero
n = 10
print(doble(n))
print(n)

Paso por referencia
Las listas y otras colecciones son datos compuestos por lo que se pasan por referencia, por lo que se los modifico desde la funcion lo modificare tambien afuera.

lista_n = [1,2,3]
print(lista_n)    
def altera_lista(lista):
    lista.append(4)
    print(lista)
altera_lista(lista_n)
print(lista_n  

Tambien se pueden modificar los tipos simples, los devolvemos modificados y se los reasignamos a su variable
def doble(numero):
    return numero * 2

n = 10
n = doble(n)
print(n)

En el caso de los tipos de datos compuestos, podemos evitar la modificacion enviando una copia
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

ns = [10,50,100]
doblar_valores(ns[:])  # Una copia al vuelo de una lista con [:]
print(ns)
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
print("asd")


def doble(numero):
    numero *= 2
    return numero
n = 10
print(doble(n))
print(n)

print("\nASD")
lista_n = [1,2,3]
print(lista_n)    
def altera_lista(lista):
    lista.append(4)
    print(lista)
altera_lista(lista_n)
print(lista_n    

