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