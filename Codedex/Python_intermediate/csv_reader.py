# Write code below 💖

import csv

with open('D:\Programacion\Python\Practica\Codedex\Python_intermediate\Bestseller - Sheet1.csv', 'r', encoding= 'utf-8') as file:
    content = csv.reader(file)

    sales = [ ]
    for index,filas in enumerate(content, start=0):
        print(filas)
        if index != 0:
            sales.append(filas[4])
        
    print('El mayor numero es:',max(sales),'millones')