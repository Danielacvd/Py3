"""
Diccionarios Python3

Se basan en una estructura mapeada donde cada elemento de la coleccion se encuentra identificado por una clave unica, por lo cual no puede haber 2 claves iguales. En otros lenguajes se conocen como arreglos asociativos.
Estos se definen iguales que los conjuntos, se usan llaves {}.

Si inicializo una variable con las llaves {} vacias las toma como dicc, pero si le annado algo, como var = {1,2} cambia a set, ya que este ya no tiene la estructura del diccionario, clave : valor .
"""

hola = {}
print(type(hola))

#Para cada elemento hay una estructura de clave:valor

animales = {'gato':'miau', 'perro':'guau'}
print(animales['gato']) #Acceso al valor de esta clave, el cual dira miau

#Los diccionarios son mutables se les puede annadir elementos a traves de sus claves

animales['gato'] = 'MIIIAUUU'
print(animales['gato'])

#Con la funcion del() puede eliminar un elemento del diccionario.
del(animales['perro'])
print(animales)

#Una de las utilidades mas grandes de los diccionarios es que podemos trabajar directamente con los valores de las claves, como si fueran variables.
edades = {'Hector':27,'Juan':45,'Maria':34}
edades['Hector']+=1
print(edades)

#Con un for puedo recorrer los elementos de un diccionario
edades = {'Hector':27,'Juan':45,'Maria':34}

for edad in edades:
    print(edad)
#Con esto se me devuelven las claves y no los valores, para solucionar esto, se tiene que indicar la clave del diccionario para cada elemento 

for clave in edades:
    print(edades[clave])

#Si queremos mostrar tanto la clave con su valor 

for clave in edades:
    print(clave,edades[clave])

#Con el metodo items() podemos leer de una forma mas facil los elemetos clave valor, devuelve ambos valores en cada iteracion automaticamente y nos permite almacenarlos.

for clave, valor in edades.items():
    print(clave, valor)       

#Listas de diccionarios
#Ambas estructuras se pueden mezclar, con los diccionarios puedo manejar las propiedades individuales de los registros, las listas nos permite manejarlos todos en conjunto.

personajes = []

gandalf = {'Nombre':'Gandalf','Clase':'Mago','Raza':'Humano'}
legolas = {'Nombre':'Legolas','Clase':'Arquero','Raza':'Elfo'}
gimli = {'Nombre':'Gimli','Clase':'Guerrero','Raza':'Enano'}

personajes.append(gandalf)
personajes.append(legolas)
personajes.append(gimli)

print(personajes)    

for pesonaje in personajes:
    print(pesonaje['Nombre'], pesonaje['Clase'], pesonaje['Raza'])
