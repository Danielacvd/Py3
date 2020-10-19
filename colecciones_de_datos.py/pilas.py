"""
Es una coleccion de elementos ordenados que solo permite 2 operaciones:
- Annadir un elemento a la pila
- Eliminar un elemento de la pila 

El ultimo elemento en entrar es el primero en salir LIFO

Si pueden crear como listas normales y annadimos elementos con el metodo append()

"""

lista = [1,2,3]
lista.append(4)
print(lista)

#Para sacar elemento usamos el metodo pop(), al usar pop() devolvemos el ultimo elemento y lo borramos

eliminado = lista.pop()
print(eliminado)
print(lista)

#Cuando ya no hay elementos en la lista y usamos el pop() dara error, ya que se encuentra vacia