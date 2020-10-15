"""
Ciclo While

inicializo variable
while condicion:
    instrucciones
    actualizar variable
else:
    print("Fin ciclo")

Si uso el break en el while, no se ejecutara el else, ya que el ciclo no finaliza su iteracion, si no que se interrumpe

Instrucción continue
Sirve para "saltarse" la iteración actual sin romper el bucle.

Hacer menus, dentro de un while van las opciones, como el do while de C
"""

i = 0
while i <= 10:
    print(i)
    i += 1
    