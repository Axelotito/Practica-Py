# Write code below 💖

from functools import reduce

''' map toma una funcion que quieras aplicar a una serie de datos y te regresa la lista con los 
datos ya transformados en esa lista '''
def divide_bu_2(x):
  return x/2

halved_numbers = map(divide_bu_2, [1,2,3,4,5,6,7,8])
print(list(halved_numbers))

''' filter toma una funcion que le da una condicion y una lista de datos que quiere checar
si tiene esa condición '''

def filter_even(x):
  return x + 2 == 4 or x + 4 == 5

even_numbers = filter(filter_even, [1,2,3,4,5,6,7,8])
print(list(even_numbers))

''' reduce '''

def multiply(x,y):
  return x * y

product = reduce(multiply, [ 1,2,3,4,5])

print(product)