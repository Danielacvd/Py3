"""
Errores y excepciones
Excepciones Multiples

Como pueden ocurrir varios tipos de errores al ejecutar un codigo, tenemos que actuar en forma diferente en cada caso.
Para estos casos lo que podemos hacer es asignar una excepcion a una variable y asi poder identificar y analizar el tipo de error que sucede gracias a un identificador.

"""
#Primer caso
try:
    n = input("Introduce un número: ")  # no transformamos a número, no usamos int() o float()
    5/n
except Exception as e:  # guardamos la excepción como una variable e
    print("Ha ocurrido un error =>", type(e).__name__)
    print(type(e))


#Cada error tiene un identificador unico, que corresponde a su tipo de dato, por lo que podemos la clase del error utlizando la syntax: print(type(e))
#nos indica que es una clase y es correcto, en python todo son clases


#Con los identificadores de errores se pueden crear multiples comprobaciones, siempre que dejemos en ultimo lugar la excepcion por defecto Exception que engloba cualquier tipo de error (si lo pone al principio las demas excepciones nunca se ejecutarian.)

try:
    n = float(input("Introduce un número divisor: "))
    5/n
except TypeError:
    print("No se puede dividir el número entre una cadena")
except ValueError:
    print("Debes introducir una cadena que sea un número")
except ZeroDivisionError:
    print("No se puede dividir por cero, prueba otro número")
except Exception as e:
    print("Ha ocurrido un error no previsto", type(e).__name__ )

