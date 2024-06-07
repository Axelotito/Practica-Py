"""
ejercicio 2 calcula el area de un 
circulo con un radio dado

"""
import math

pi = math.pi 
radio = float(input())

area = pi * radio ** 2
print(f"El area del circulo es {area:.2f}")

""" Al parecer tengo que poner una f al inicio del print para que funcione """
