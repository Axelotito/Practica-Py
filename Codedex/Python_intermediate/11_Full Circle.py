from math import pi
""" pure functions es una función cuya salida se 
deriva únicamente de sus valores de entrada """

def pure_function(number):
    return number ** 2

""" las funciones puras no utilizan variables globales
sino solo variables que mete el usuario"""

def impure_function(number):
    result = number ** 2
    print(f'The square of {number} is {result}')
    return result

impure_function(4)

""" ejercicio has una funcion pura que calcule el radio del circulo """

def calculate_circle_area(radius):
    result = radius ** 2 * pi
    return result

print(calculate_circle_area(5))

""" 
Para que sea una funcion pura tiene que cumplir con 
1. Siempre produce el mismo resultado dado el mismo conjunto de entradas
2.No tiene efectos secundarios, es decir, no modifica variables fuera de
su alcance ni interactúa con el mundo exterior (como leer o escribir archivos,
modificar variables globales, etc.).
"""