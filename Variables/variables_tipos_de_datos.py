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