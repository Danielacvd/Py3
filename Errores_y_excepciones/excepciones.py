"""
Errores y Excepciones en Python
Excepciones
Son bloques de codigo que nos permiten seguir con la ejecucion del codigo a pesar de que tengamos un error.

Bloque Try-Except
Para prevenir fallos/errores tenemos que poner el bloque propenso a errores en un bloque TRY, y luego encadenar un bloque except para tratar la situacion excepcional, mostrando que ocurrio un fallo/error

try:
    n = float(input("Introduce un número decimal: "))
    m = 4
    print("{}/{} = {}".format(n,m,n/m))
except:
    print("Ha ocurrido un error, introduce bien el número")

De esta forma se controlar situaciones excepcionales que generan errores y en vez de que se muestre el error mostramos un mensaje o ejecutamos una pieza de codigo diferente.
Tambien al usar excepciones se puede forzar al usuario a introducir un numero valida usando un while, haciendo que introduzca el dato solicitado hasta que lo haga bien, y romper el ciclo con un break.
while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{} = {}".format(n,m,n/m))
        break  
    except:
        print("Ha ocurrido un error, introduce bien el número")

Bloque else:
Puedo encadenar un bloque else despues del except (similar al else de un ciclo) para comprobar el caso en que todo salio bien.(Si todo funciona bien, no se ejecuta la excepcion).

while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{} = {}".format(n,m,n/m))
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        print("Todo ha funcionado correctamente")
        break  


Bloque Finally:
Este bloque se ejecutara al final del codigo, ocurra o no un error
while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{} = {}".format(n,m,n/m))
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        print("Todo ha funcionado correctamente")
        break  
    finally:
        print("Fin de la iteración") 

"""
try:
    n = float(input("Introduce un número decimal: "))
    m = 4
    print("{}/{} = {}".format(n,m,n/m))
except:
    print("Ha ocurrido un error, introduce bien el número")

while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{} = {}".format(n,m,n/m))
        break  
    except:
        print("Ha ocurrido un error, introduce bien el número")    


while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{} = {}".format(n,m,n/m))
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        print("Todo ha funcionado correctamente")
        break          