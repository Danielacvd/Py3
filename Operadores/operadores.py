"""
Aritmeticos

Suma: +
Resta: -
Multiplicacion: *
Division: /
Division Entera: //
Modulo de la division: %
Potencia: **

"""

"""
Logicos

y: and
o: or 
negacion: not (Niego una expresion logica o un valor, invierto una verdad, doy vuelta un resultado, una comparacion)

"""

"""
Incremente/Decremento

y += 1
y *= 1
y /= 1
y **= 1
y -=1

"""

"""
Operadores de comparacion

igual: ==
distinto: !=
menor: <
menor igual: <=
mayor: >
mayor igual: >=

"""

"""
True equivale a 1
False equivale a 0
"""

"""
Siempre puedo ir anidando todas estas expresiones
"""


print("*** Ejercicio 1 ***")

"""
Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):

Si los dos números son iguales
Si los dos números son diferentes
Si el primero es mayor que el segundo
Si el segundo es mayor o igual que el primero
"""

n1 = int(input())
n2 = int(input())
if n1 == n2:
    print("Si los 2 numeros son iguales")

if n1 != n2:
    print("Si los 2 numeros son diferentes")    

if n1 > n2:
    print("Si el primero es mayor que el segundo") 

if n1 < n2:
    print("Si el segundo es mayor que el primero")       


print("*** Ejercicio 2 ***")

"""
Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False).
"""

frase = input("Ingresa tu frase: ")

if len(frase) >= 3 and len(frase) < 10:
    print(f"Si lo es: {frase}")

print("*** Ejercicio 3 ***")
"""
Ejercicio 3
Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

Guarda en una variable numero_magico el valor 12345679 (sin el 8)
Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
Multiplica el numero_usuario por 9 en sí mismo
Multiplica el numero_magico por el numero_usuario en sí mismo
Finalmente muestra el valor final del numero_magico por pantalla
"""

numero_magico = 12345679
numero_user = int(input())
numero_user *= 9
numero_magico *= numero_user
print(numero_magico)