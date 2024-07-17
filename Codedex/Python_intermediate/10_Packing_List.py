import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try: 
    with open('packing_list.csv', 'r', encoding= 'utf-8') as file: 
        