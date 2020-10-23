"""
Funciones Python3
Funciones Integradoras
La libreria standar de Python incluye muchas funciones, para hacer conversiones entre tipos de datos, matematicas, utilidades, entre muchas otras.

Algunos ejemplos:
int() nos sirve para transformar una cadena de texto a entero(en caso de que no se pueda ejecutar la instruccion dara error)
numero = int("20"), type(numero) #=> int

float() nos sirve para transformar una cadena de texto a flotante, al igual que int() si no puede hacer la transformacion dara un error.
decimal = float(10), print(decimal) #=> 10.0, type(decimal) #=> float

str() transforma cualquier valor a una cadena de texto
cadena = str(10), print(cadena) #=> "10", type(cadena) #=>str

bin() conversion de entero a binario
bin(10) #=> '0b1010'

hex() conversion de entero a decimal
hex(10) #=> '0xa'

int(numero, base) reconversion a entero(base 10)
print(int('0b1010', 2)) #=> 10
print(int('0xa', 16)) #=> 10

abs() nos da el valor absoluto de un numero (distancia??)
abs(-10) #=> 10

round() redondeo de un numero flotante a entero, menor de .5 a la baja, mayor o iguala 5 a la alza.
print(round(5.5)) #=> 6
print(round(5.4)) #=> 5

eval() evalua una cadena, como una expresion, acepta variables si se ha definido anteriormente
eval('2 + 5') #=> 7
n = 10
eval('n * 10 - 5') #=> 95

len() longitud de una coleccion o cadena
print(len("Una cadena")) #=> 10

help() invoca el menu de ayuda del interprete de Python



"""