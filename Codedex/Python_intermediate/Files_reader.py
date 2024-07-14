file = open('example.txt', 'w')

file.write('Hello World\n')
file.write('This is our new text file\n')
file.write('Hola que tal\n')

file2 = open('.\Codedex\Python_intermediate\Example_file_reader.txt', 'w')

lines = [ 'hola esto', '\nes una', '\nlinea nueva']
file2.writelines(lines)
file2.close()

file2 = open('.\Codedex\Python_intermediate\Example_file_reader.txt', 'r')
print('using read() method: ')
content = file2.read()
print(content)
file2.close()

""" 
Esto que se hace con with es para que no tengas que colocar el close()
al final del archivo, ya que con with se cierra automaticamente 
"""

with open('.\Codedex\Python_intermediate\Example_file_reader.txt', 'w') as file3: 
    file3.write('Esto est un texto que va a modificar el archivo')

with open('.\Codedex\Python_intermediate\Example_file_reader.txt', 'r') as file3:
    content = file3.read()
    print(content)