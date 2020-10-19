"""
Otra forma para que podamos introducir una cierta cantidad de datos es usando una lista, pero tenemos que saber desde antes cuantos seran los datos que ingresaremos, usaremos una lista vacia
"""
lista_de_datos = []
for x in range(5):
    lista_de_datos.append(input("Introduce un dato: "))

print(lista_de_datos)
for i in lista_de_datos:
    print(i)    