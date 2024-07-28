import csv
import random

# Leer el archivo CSV
with open('D:\Programacion\Python\Practica\Codedex\Python_intermediate\Horarios.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Leer la primera fila como encabezados
    data = list(reader)  # Leer el resto del archivo

# Función para verificar si hay empalme entre dos horarios
def hay_empalme(horario1, horario2):
    dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
    for dia in dias:
        if horario1[dia] != 'NO' and horario2[dia] != 'NO':
            try:
                inicio1, fin1 = map(lambda x: int(x.replace(':', '')), horario1[dia].split(' - '))
                inicio2, fin2 = map(lambda x: int(x.replace(':', '')), horario2[dia].split(' - '))
                if not (fin1 <= inicio2 or fin2 <= inicio1):
                    return True
            except ValueError:
                continue  # Ignorar horarios mal formateados
    return False

# Procesar los datos para obtener una lista de materias con sus horarios
materias = []
for row in data:
    materia = {
        'profesor': row[0],
        'codigo': row[1],
        'nombre': row[2],
        'aula': row[3],
        'Lunes': row[4].split(':')[1].strip() if 'Lun' in row[4] else 'NO',
        'Martes': row[5].split(':')[1].strip() if 'Mar' in row[5] else 'NO',
        'Miercoles': row[6].split(':')[1].strip() if 'Mie' in row[6] else 'NO',
        'Jueves': row[7].split(':')[1].strip() if 'Jue' in row[7] else 'NO',
        'Viernes': row[8].split(':')[1].strip() if 'Vie' in row[8] else 'NO'
    }
    materias.append(materia)

# Generar 10 horarios aleatorios sin repetir materias
horarios_aleatorios = []
for _ in range(10):
    horario = []
    materias_disponibles = materias[:]
    while materias_disponibles:
        materia = random.choice(materias_disponibles)
        if all(not hay_empalme(materia, m) for m in horario) and materia['nombre'] not in [m['nombre'] for m in horario]:
            horario.append(materia)
        materias_disponibles.remove(materia)
    horarios_aleatorios.append(horario)

# Escribir los horarios aleatorios en un archivo CSV
with open('Horarios_Aleatorios.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Escribir los encabezados
    for horario in horarios_aleatorios:
        for materia in horario:
            writer.writerow([
                materia['profesor'],
                materia['codigo'],
                materia['nombre'],
                materia['aula'],
                f"Lun:{materia['Lunes']}",
                f"Mar:{materia['Martes']}",
                f"Mie:{materia['Miercoles']}",
                f"Jue:{materia['Jueves']}",
                f"Vie:{materia['Viernes']}"
            ])
        writer.writerow([])  # Escribir una fila vacía entre horarios