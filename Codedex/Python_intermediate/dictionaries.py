# Write code below 💖
''' diccionario '''
diccionario = { 
  'llave1' : 2,
  'llave2' : 4,
  'llave3' : 6,
  'llave4' : 5
}

print(diccionario['llave3'])

student_info = {'name' : 'Axel', 'age': 9, 'grade' : 'A'}

print(student_info['name'])
print(student_info['age'])
print(student_info['grade'])

''' para modificar '''

student_info['age'] = 19

print(f"update age {student_info['age']}")

''' metodos de los diccionarios '''

print(f'keys: {student_info.keys()}')
print(f'values: {student_info.values()}')
print(f'Items: {student_info.items()}')

for i in zip(student_info.keys(), student_info.values()): 
  print(i)

print('')

museo = { 'artist' : '' , 'period' : '' , 'date' : 0 }

museo['artist'] = 'Miguel Angel'
museo[ 'period' ] = 'Renacimiento'
museo['date'] = '1511'

print(museo)
print(f'keys: {museo.keys()}')
print(f'values: {museo.values()}')