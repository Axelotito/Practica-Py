import random 
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def create_fantasy_name(list_1, list_2):
  return random.choice(list_1) + ' ' + random.choice(list_2)

print(create_fantasy_name(prefixes, suffixes))

def capitalize_suffix(suffix):
  name_capitalized = suffix[0].upper() + suffix[1:]
  return name_capitalized

list_capitalized_suffix = list(map(capitalize_suffix, suffixes))

def fire_in_name(name):
  return 'Fire' in name or 'fire' in name

def concatenate_names(name1,name2):
  return name1 + name2

"""
Displays information about generated fantasy names.
This function generates a list of fantasy names using the `create_fantasy_name` function.
It then filters the names to only include those that contain the word "fire" using the `fire_in_name` function.
Finally, it concatenates the filtered names using the `concatenate_names` function.
"""
def display_name_info():
  random_names = []
  [random_names.append(create_fantasy_name(prefixes,suffixes)) for i in range(10)]
  names_fire = list(filter(fire_in_name, random_names))
  concatenated_names = reduce(concatenate_names,names_fire)

  print('Generates Fantasy Names:', [names for names in names_fire])
  print('Names with Fire:',names_fire)
  print("Concatenated names:", concatenated_names)

display_name_info()