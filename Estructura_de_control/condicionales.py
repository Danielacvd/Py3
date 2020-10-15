"""
Estructura de control If, elif, else, siempre que una condicion sea verdadera se entrara en el if

if True:  equivale a if not False
if a[0]:

Instrucción pass
Sirve para finalizar un bloque, se puede utilizar en un bloque vacío:

if True:
    pass

"""

n1 = 10
n2 = 15
n3 = 20

if n1 > n2:
    print(True)
else:
    print(False)

if n1 > n2 and n1 > n3:
    print(f"N1: {n1} es mayor")
elif n2 > n2 and n2 > n3:
    print(f"N2: {n2} es mayor")
else:
    print(f"N3: {n3} es el mayor")    
