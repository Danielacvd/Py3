"""
Ejercicios Sobre colecciones de datos


"""

print("*** Ejercicio 1 ***")
"""
Realiza un programa que siga las siguientes instrucciones:

Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
Crea un conjunto llamado administradores con los administradores Juan y Marta.
Borra al administrador Juan del conjunto de administradores.
Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no.
"""

usuarios = {'Marta', 'David', 'Elvira', 'Juan', 'Marcos'}
administradores = {'Juan', 'Marta'}

administradores.discard('Juan')
administradores.add('Juan')

for usuario in usuarios:
    if not usuario in administradores:
        print(f"El usuario: {usuario} no es administrador")
    else:
        print(f"El usuario: {usuario} es administrador")    

print("*** Ejercicio 2 ***")
"""
Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase de personaje jugable. Partiendo que la estadística base es 2, debes cumplir las siguientes condiciones:

El caballero tiene el doble de vida y defensa que un guerrero.
El guerrero tiene el doble de ataque y alcance que un caballero.
El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance.
Muestra como quedan las propiedades de los tres personajes.
"""

# .discard(elemento) sirve para borrar o descartar un elemento.

caballero = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
guerrero  = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
arquero   = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
#Todos son diccionarios

#edades = {'Hector':27,'Juan':45,'Maria':34}
#edades['Hector']+=1

caballero['vida'] = guerrero['vida'] * 2
caballero['defensa'] = guerrero['defensa'] * 2
guerrero['ataque'] = caballero['ataque'] * 2
guerrero['alcance'] = caballero['alcance'] * 2
arquero['vida'] = guerrero['vida']
arquero['ataque'] = guerrero['ataque']
arquero['defensa'] = guerrero['defensa'] / 2
arquero['alcance'] = guerrero['alcance'] * 2

print("El caballero tiene")
for i in caballero:
    print(i,caballero[i])

print("El guerrero tiene")   
for i in guerrero: 
    print(i,guerrero[i])

print("El arquero tiene")   
for i in arquero: 
    print(i,arquero[i])

print("*** Ejercicio 3 ***")
"""
Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).

¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?
"""
from collections import deque
tareas = [ 
    [6, 'Distribución'],
    [2, 'Diseño'],
    [1, 'Concepción'],
    [7, 'Mantenimiento'],
    [4, 'Producción'],
    [3, 'Planificación'],
    [5, 'Pruebas']
]

print("lista desordenada")
for tarea in tareas:
    print(tarea[0], tarea[1])


from collections import deque
#el metodo .sort() al ser mostrado dentro de un print nos dire NONE
tareas.sort()
print(tareas)
cola = deque()
for tarea in tareas:
    cola.append(tarea[1])

print("lista ordenada")
for tarea in cola:
    print(tarea)

