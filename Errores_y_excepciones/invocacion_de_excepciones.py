"""
Errores y Excepciones Python3
Invocacion de excepciones
Por si necesitamos llamar a un error manualmente y no usar un simple print()

Instruccion Raise
Con raise se puede lanzer un error manual pasandole el identificador. Luego annadimos un except para tratar esta excepcion que se hemos lanzado.


"""

def mi_funcion(algo=None):
    if algo is None:
        print("Error no se permite un valor nulo (con un print)")

mi_funcion()

#Con Raise

def mi_funcion(algo=None):
    try:
        if algo is None:
            raise ValueError("Error! No se permite un valor nulo")
    except ValueError:
        print("Error! No se permite un valor nulo (desde la excepción)")

mi_funcion()

