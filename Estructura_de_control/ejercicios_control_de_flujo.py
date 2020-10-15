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