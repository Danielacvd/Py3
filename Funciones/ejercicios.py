"""
Ejercicios de Funciones Python

"""
from math import pi

print("*** Ejercicio 1 ***")
"""
Realiza una función llamada area_rectangulo(base, altura) que devuelva el área del rectangulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura:
El área de un rectángulo se obtiene al multiplicar la base por la altura.

"""

def area_rectangulo(base, altura):
    area = base * altura
    return area

print( area_rectangulo(15,10))    


print("*** Ejercicio 2 ***")
"""
Realiza una función llamada area_circulo(radio) que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio:
El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi

"""
def area_circulo(radio):
    area = (radio**2)*pi
    return area

print(round(area_circulo(5),3))    


print("*** Ejercicio 3 ***")
"""
Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo siguiente:

Si el primer número es mayor que el segundo, debe devolver 1.
Si el primer número es menor que el segundo, debe devolver -1.
Si ambos números son iguales, debe devolver un 0.
Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'.

"""

def relacion(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    elif a == b:
        return 0

print(relacion(5,10))
print(relacion(10,5))
print(relacion(5,5))


print("*** Ejercicio 4 ***")
"""
Realiza una función llamada intermedio(a, b) que a partir de dos números, devuelva su punto intermedio. Cuando lo tengas comprueba el punto intermedio entre -12 y 24:
El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

"""

def intermedio(a, b):
    intermedio = (a+b)/2
    return intermedio
print(intermedio(-12, 24))    



print("*** Ejercicio 5 ***")
"""
Realiza una función llamada recortar(numero, minimo, maximo) que reciba tres parámetros. El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:

Devolver el límite inferior si el número es menor que éste
Devolver el límite superior si el número es mayor que éste.
Devolver el número sin cambios si no se supera ningún límite.
Comprueba el resultado de recortar 15 entre los límites 0 y 10.

"""

def recortar(numero, minimo, maximo):
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    elif numero == minimo and numero == maximo:
        return numero

print(recortar(15, 0, 10))                


print("*** Ejercicio 6 ***")
"""
Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.

"""
numeros = [-12, 84, 13, 20, -33, 101, 9]

def separar(lista):
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares

print(separar(numeros))             
         