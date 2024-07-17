import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try: 
    with open('D:\Programacion\Python\Practica\Codedex\Python_intermediate\packing_list.csv', 'r', encoding= 'utf-8') as file: 
        archivo = csv.reader(file)
        for filas in archivo:
            print(filas)
except FileNotFoundError: 
    print("Packing list file not found. Creating a new one.")
    with open('D:\Programacion\Python\Practica\Codedex\Python_intermediate\packing_list.csv', 'w', encoding= 'utf-8') as file:
        archivo = csv.writer(file)
        archivo.writerows(data)