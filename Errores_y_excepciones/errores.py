"""
Errores en Python3
Un error nos detiene la ejecucion de un programa, teniendo varias causas.

Errores de Syntax:
SyntaxError, se dan como por ejemplo no cerrar bien un print("hola", nos dara error de Syntax
SyntaxError: unexpected EOF while parsing

Errores de nombre:
NameError, se da cuando escribimos mal una palabra, pint("hola")
NameError: name 'pint' is not defined

Errores semanticos:
Van ligados al sentidodel funcionamiento y dependen de la situacion, pop() a una lista vacia de error, esta situacion ocurre solo cuando ejecutamos el programa, el editor no nos avisara, lista = [], lista.pop()
IndexError: pop from empty list
Para prevenir este tipo de error, nos podemos asegurar de que la lista no esta vacia, podemos usar el metodo len().
if len(l) > 0:
    l.pop()
Otro ejemplo es cuando a traves de input obtenemos datos del usuario y si los queremos operar (como hacer una suma) vamos a tener un error de tipo de dato
TypeError: unsupported operand type(s) for /: 'str' and 'int', ejemplo.
Aunque tambien puede pasar al reves, quiero un numero y me dan un texto, aunque este haciendo int() me dara error..






"""