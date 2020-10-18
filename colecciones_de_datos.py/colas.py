"""
Son colecciones de elementos ordenados que permiten solo 2 acciones

- Annadir un elemento a la cola
- Sacar un elementos de la cola

El primer elemento en entrar es el primero en salir, FIFO

Para hacer una cola tenemos que importar un modulo, para crear la cola

"""

from collections import deque
cola = deque()
print(cola)
#deque([])

#Podemos annadir elementos al crear la cola, pasando una lista
#cola = deque([1,2,'Daniel'])
#Luego podemos annadir elementos con el metodo .append()
cola.append(2)
cola.append('Daniel')
print(cola)

#Para sacar los elementos podemos usar el metodo popleft(), es lo mismo que el pop(), pero este metodo extrae elementos por la parte izquierda, el cual es el principio de la cola.

print(cola.popleft())  #Devuelvo el 2 y lo borro de la cola
print(cola)            #Solo queda 'Daniel'


