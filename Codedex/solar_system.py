from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)
if random_planet == 'Mercury':
  r = 2440
elif random_planet == 'Venus':
  r = 6052
elif random_planet == 'Earth':
  r = 6371 
elif random_planet == 'Mars':
  r = 3390
elif random_planet == 'Saturn':
  r = 58232
else:
  print('Ooops! An error occurred.')

area = int(4*pi*r*r)

print(f'El planeta es: {random_planet} \nEl area es: {area}')