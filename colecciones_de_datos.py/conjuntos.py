"""
Conjuntos en Python3

Son colecciones DESORDENADAS de ELEMENTOS UNICOS, se usa para hacer pruebas de pertenencia a grupos y eliminacion de elemetos duplicados.

Su Syntax:
conjunto = set()
o
conjunto = {}


"""

#Metodo add(), annade un elemento si no lo encuentra dentro del cunjunto
conjunto = {1,2,3}
print(type(conjunto))
conjunto.add(4)
print(conjunto)
conjunto.add(4)
print(conjunto)
#El ultimo 4 no se annadio ya que ya hay un 4 dentro del conjunto.
#Ademas que este 4, no necesariamente lo incluira en la ultima posicion, lo dejare en cualquier parte xd.


#Para verificar si un elemento pertenece a un conjunto podemos usar la sintaxis in, 

print('Daniel' in conjunto)
#in retorna True o False

conjunto.add('Daniel')
print('Daniel' in conjunto)
print(conjunto)
print('Daniel' not in conjunto)
# Tambien se puede usar de la misma forma que el in, el not in

#Los conjuntos no pueden tener el mismo elementos mas de una vez, no adminte elementos duplicados, se borran automaticamente.

#Conversion con listas

lista = [11,1,1,2,3,4,54,34,3,3,3,3]
conjunto_2 = set(lista)
print(lista)
print(conjunto_2)

#Conversion con cadenas
#Hacer esta conversion nos permitira sacar todos los caracteres dentro de una cadena, sin los duplicados.

cadena = 'Al pan pan y al vino vino'
cadena_2 = set(cadena)
print(cadena_2)
print(type(cadena_2))