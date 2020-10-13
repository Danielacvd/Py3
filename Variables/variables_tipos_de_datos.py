"""
Variables y Tipos de Datos

"""

texto = "Soy un texto"
numero = 10
decimal = 10.5
verdadero = True
numero2 = f"{numero} y {decimal}"
numero3 = numero + 1
nombre = "Daniel"
# Formas de imprimir
print(numero)
print(f"{numero}")
print(":",numero)
print("Numero decimal " + str(decimal) + " Numero entero: " + str(numero))
print(r"cd\nhola")
print(f"{nombre*2}")

#Las cadenas no son mutables
#nombre[0] = 'J', no puedo hacer Janiel
print(len(nombre))
#Concatenar 
print(f"Los numeros son: {numero} y {decimal}")
print("El numero decimal es:",decimal)

#Tipos de datos
print(type(numero))
print(type(decimal))
print(type(verdadero))

#Cambiar tipo de dato
numero_deicmal = 10
print(type(numero_deicmal))
numero_decimal = float(10)
print(type(numero_decimal))


#Ejercicios
print("\n*** Ejercicios 1 ***")
"""

Ejercicio 1
Identifica el tipo de dato (int, float, string o list) de los siguientes valores literales:
"Hola Mundo"     
[1, 10, 100]      
-25              
1.167             
["Hola", "Mundo"] 
' '    
"""
saludo = "Hola Mundo"
lista = [1, 10, 100]
negativo = -25
decimal = 1.167
lista_2 = ["Hola", "Mundo"]
comillas = ' '

print(type(saludo)) #str
print(type(lista))  #list
print(type(decimal)) #float
print(type(lista_2)) #list
print(type(comillas)) #string

print("\n*** Ejercicios 2 ***")
"""
Ejercicio 2
Determina mentalmente (sin programar) el resultado que aparecerá por pantalla en las siguientes operaciones con variables:

a = 10
b = -5
c = "Hola "
d = [1, 2, 3] 

print(a * 5)  #50
print(a - b)  #15
print(c + "Mundo") #Hola mundo
print(c * 2) #"Hola Hola
print(d[-1]) #3
print(d[1:]) #2,3
print(d + d) # [1,2,3,1,2,3]  

"""
a = 10
b = -5
c = "Hola "
d = [1, 2, 3] 

print(a * 5)  #50
print(a - b)  #5
print(c + "Mundo") #Hola mundo
print(c * 2) #"Hola Hola
print(d[-1]) #3
print(d[1:]) #2
print(d + d) # [1,2,3,1,2,3]  


print("\n*** Ejercicios 3 ***")

"""
Ejercicio 3
El siguiente código pretende realizar una media entre 3 números, pero no funciona correctamente. ¿Eres capaz de identificar el problema y solucionarlo?
numero_1 = 9
numero_2 = 3
numero_3 = 6

media = numero_1 + numero_2 + numero_3 / 3
print("La nota media es", media)
"""
numero_1 = 9
numero_2 = 3
numero_3 = 6

media = numero_1 + numero_2 + numero_3 / 3
print("La nota media es", media)
#Deberia ser 6

media = (numero_1 + numero_2 + numero_3) / 3
print("La nota media es", media)

print("\n*** Ejercicios 4 ***")

"""
Ejercicio 4
A partir del ejercicio anterior, vamos a suponer que cada número es una nota, y lo que queremos es obtener la nota final. El problema es que cada nota tiene un valor porcentual:

La primera nota vale un 15% del total
La segunda nota vale un 35% del total
La tercera nota vale un 50% del total
Desarrolla un programa para calcular perfectamente la nota final:

nota_1 = 10
nota_2 = 7
nota_3 = 4
"""

nota_1 = 10*0.15
nota_2 = 7*0.35
nota_3 = 4*0.50
nota_final = (nota_1+nota_2+nota_3)
print(nota_final)

print("\n*** Ejercicios 5 ***")

"""
Ejercicio 5
La siguiente matriz (o lista con listas anidadas) debe cumplir una condición, y es que en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?

matriz = [ 
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]

"""

matriz = [ 
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]
matriz[1][-1] = sum(matriz[1][:-1])
matriz[3][-1] = sum(matriz[3][:-1])
print(matriz)

print("\n*** Ejercicios 6 ***")


"""
Ejercicio 6
Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?
Nombre Apellido ha sacado un Nota de nota.
"""

cadena = "zeréP nauJ,01"

#print(cadena[::-1])
cadena_volteada = cadena[::-1]
print(cadena_volteada[3:], "ha sacado un", cadena_volteada[:2], "de nota.")