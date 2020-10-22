"""
Funciones en Python
Funciones Recursivas
Es una funcion que se llama a si misma durante su ejecucion, es una forma de iterar, pero se tiene que planificar el momento en que dejan de llamarse a si mismas, si no se corta estara iterando por siempre.

(Suele usarse para dividir una tarea en subtareas mas simples de forma que sea mas facil abordar el problema y solucionarlo.)

Ejemplo sin Retorno
Cuanta regresiva de un numero hasta 0.
def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Boooooooom!")
    print("Fin de la función", num)

cuenta_atras(5)

Ejemplo con retorno:
El factorial de un numero corresponde al producto de todos los numeros desde 1 hasta el propio numero
3! = 1 x 2 x 3 = 6
5! = 1 x 2 x 3 x 4 x 5 = 120

def factorial(num):
    print("Valor inicial ->",num)
    if num > 1:
        num = num * factorial(num -1)
    print("valor final ->",num)
    return num

print(factorial(5))

"""

def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Boooooooom!")
    print("Fin de la función", num)

cuenta_atras(5)

def factorial(num):
    print("Valor inicial ->",num)
    if num > 1:
        num = num * factorial(num -1)
    print("valor final ->",num)
    return num

print(factorial(5))