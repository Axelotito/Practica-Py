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

''' excersice '''
# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.8), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

def longer_than_five_minutes(x):
 return x[1] >= 5.00 

songs = filter(longer_than_five_minutes, playlist)
print("Canciones de mas de 5 min:",list(songs))

def minutes_to_seconds(x):
  return x[1] * 60 

songs_in_seconds = map(minutes_to_seconds, playlist) 
print('segundos de las canciones:',list(songs_in_seconds))

def add_durations(total,song):
  return total + song[1]

total = reduce(add_durations, playlist, 0)
print("La suma es de:", total)