"""
Tuplas en Python3
Son variables contenedoras parecidas a las listas, pero las tuplas son inmutables
"""

tupla = (100,"Hola",[1,2,3],-50)

print(tupla)
print(tupla[0])
print(tupla[-1])
print(tupla[2:])
print(tupla[2][-1])

#Funcion index() para saber la posicion de un elemento en la tupla
print(tupla.index(100))
#Si no lo encuentra enviara un error
#con count() puedo contar cuantas veces aparece un elemento en la tupla
print(tupla.count(100))
#Si busca algo que no esta dentro de la tupla, no da error, dira 0
#No disponen del metodo append()