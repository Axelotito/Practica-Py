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

with open('.\Codedex\Python_intermediate\Bestseller_info.cvs', 'w', encoding= 'utf-8') as file:
    csv_write = csv.writer(file)
    """ 
    .writer() sirve para crear un objeto que nos permitira escribir en el archivo csv 
    mientras que .writerow() nos permite escribir una fila en el archivo csv
    """
    csv_write.writerow(['Book', 'Author', 'Sales in millions'])