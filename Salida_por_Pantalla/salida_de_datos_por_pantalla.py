"""
Salida de datos por pantalla
Varias formas:
Con print() podemos mostrar infomacion por pantalla, tanto texto, como variables de los programas


"""

var1 = 10
var2 = 5

print("Un dia ", var1, "Del mes", var2)

#Esta el metodo format(), este nos permite formatear informacion dentro de una cadena de texto
v = "otro texto"
n = 10
c = "Un texto '{}' y un número '{}'".format(v,n)
print(c)

#Tambien se puede referenciar a partir de la posicion de los valores usando indices
print( "Un texto '{1}' y un número '{0}'".format(v,n) )
print(c)

#se puede usar un identificador con una clave y luego pasarlas en el format
print( "Un texto '{v}' y un número '{n}'".format(n=n,v=v) )

#Formateo AVANZADO, el metodo format(), soporta muchas tecnicas de formateo
#Alineamiento a la derecha de 30 caracteres
print( "{:>30}".format("palabra") )  

#Alineamiento a las izquierda de 30 caracteres(creo espacios a la derecha)
print( "{:30}".format("palabra") )

#Alineamiento al centro de 30 caracteres
print( "{:^30}".format("palabra") ) 

#truncamiento de 3 caracteres
print( "{:.3}".format("palabra") )  

#alineamineto a la derecha de 30 caracteres con trunctamiento de 3 caracteres
print( "{:>30.3}".format("palabra") )  

#formateo de numero enteros, rellenados con espacios
print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))
print("{:4d}".format(1))

#formateo de numero enteros, rellenados con ceros
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

#formateo de numero flotantes, rellenados con espacios
print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(153.21))

#formateo de numeros flotantes, rellenados con ceros
print("{:07.3f}".format(3.1415926))
print("{:07.3f}".format(153.21))


nombre = 'Daniel'
apellido = 'Paredes'
nombre_completo = f"{nombre} {apellido}"
print(nombre_completo)
