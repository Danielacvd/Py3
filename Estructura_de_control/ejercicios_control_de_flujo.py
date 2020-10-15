print("*** Ejercicio 1 ***")
"""
Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
En caso de introducir una opción inválida, el programa informará de que no es correcta.
"""

n1 = int(input())
n2 = int(input())

while True:
    print("""
    1) Mostrar la suma de los 2 numeros
    2) Mostrar la resta de los 2 numeros (el primero menos el segundo)
    3) Mostrar la multiplicacion de los 2 numeros 
    4) Para salir
    """)
    opcion = input()
    if opcion == '1':
        print(f"La suma es: {n1+n2}")
    elif opcion == '2':
        print(f"La resta es: {n1-n2}")
    elif opcion == '3':
        print(f"La multiplicacion es: {n1*n2}") 
    elif opcion == '4':
        break     
    else:
        print("La opcion no es correcta")      
else:
    print("Fin ciclo")


print("*** Ejercicio 2 ***")

"""
Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente.
"""

numero = int(input())

while numero % 2 != 1:
    print(f"El numero {numero} es par")
    numero = int(input())

print("*** Ejercicio 3 ***")

"""
Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100.
"""
contador = 0
for i in range(1, 101):
    if i % 2 == 0:
        contador += i
else:
    print("Fin ciclo for")

print(f"La suma es {contador}")  

#Otra forma

suma = sum(range(0, 101, 2))
print(suma)

print("*** Ejercicio 4 ***")

"""
Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética.
"""

numeros = int(input("Introduce la cantidad de numeros que quieres entregar: "))

i = 0
contador = []
while i < numeros:
    contador.append(int(input()))
    i += 1
resultado = sum(contador)/len(contador)
print(f"La suma de los {len(contador)} es {sum(contador)} y la media aritmetica es {resultado}") 

print("*** Ejercicio 5 ***")

"""
Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
"""

lista = [0,1,2,3,4,5,6,7,8,9]


while True:
    numero = int(input("Introduce un numero: "))
    if numero in lista:
        print(f"El numero {numero}, si esta en la lista")
        break
else:
    print("Ingresa otro numero")

print("*** Ejercicio 6 ***")

"""
Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

Todos los números del 0 al 10 [0, 1, 2, ..., 10]
Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

"""

lista_1 = list(range(0, 11)) 
lista_2 = list(range(-10, 1, 1))
lista_3 = list(range(0, 21, 2))
lista_4 = list(range(-19, 1, 2))
lista_5 = list(range(0, 51, 5))
print(lista_1)
print(lista_2)
print(lista_3)
print(lista_4)
print(lista_5)