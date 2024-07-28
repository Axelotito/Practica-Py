import pandas as pd
import random

# Ruta del archivo CSV
ruta_csv = r'D:\Programacion\Python\Practica\Codedex\Python_intermediate\Horarios.csv'

try:
    df = pd.read_csv(ruta_csv)
except FileNotFoundError:
    print(f"El archivo en la ruta {ruta_csv} no fue encontrado.")
    exit()

# Eliminar espacios en blanco de los nombres de las columnas
df.columns = df.columns.str.strip()

# Renombrar las columnas incorrectas
df = df.rename(columns={'Martes-end    .1': 'Miercoles-end'})

# Asegurar que los nombres de las columnas sean los esperados
columnas_esperadas = ['Maestro', 'Clave', 'Materia', 'Grupo', 'Lunes', 'Lunes-end', 'Martes', 'Martes-end', 
                      'Miercoles', 'Miercoles-end', 'Jueves', 'Jueves-end', 'Viernes', 'Viernes-end']

# Verificar si las columnas del CSV coinciden con las esperadas
columnas_actuales = df.columns.tolist()
if not all(col in columnas_actuales for col in columnas_esperadas):
    print("El archivo CSV no tiene las columnas esperadas.")
    print(f"Columnas encontradas: {columnas_actuales}")
    print(f"Columnas esperadas: {columnas_esperadas}")
    exit()

# Eliminar filas duplicadas basadas en las columnas 'Maestro' y 'Materia'
df = df.drop_duplicates(subset=['Maestro', 'Materia'])

# Función para generar un horario sin repetir materias
def generar_horario(df):
    horario = []
    materias_agregadas = set()
    df_shuffled = df.sample(frac=1).reset_index(drop=True)  # Mezclar el DataFrame
    maestros = df_shuffled['Maestro'].unique()
    for maestro in maestros:
        clases_maestro = df_shuffled[df_shuffled['Maestro'] == maestro]
        for index, clase in clases_maestro.iterrows():
            if clase['Materia'] not in materias_agregadas:
                horario.append({
                    'Maestro': clase['Maestro'],
                    'Clave': clase['Clave'],
                    'Materia': clase['Materia'],
                    'Grupo': clase['Grupo'],
                    'Lunes': clase['Lunes'],
                    'Lunes-end': clase['Lunes-end'],
                    'Martes': clase['Martes'],
                    'Martes-end': clase['Martes-end'],
                    'Miercoles': clase['Miercoles'],
                    'Miercoles-end': clase['Miercoles-end'],
                    'Jueves': clase['Jueves'],
                    'Jueves-end': clase['Jueves-end'],
                    'Viernes': clase['Viernes'],
                    'Viernes-end': clase['Viernes-end']
                })
                materias_agregadas.add(clase['Materia'])
    return horario

# Generar 10 horarios diferentes
horarios = []
for _ in range(10):
    horario = generar_horario(df)
    horarios.append(horario)

# Convertir los horarios a DataFrame y agregar una fila vacía después de cada 5 materias
def agregar_fila_vacia(horario):
    if not horario:
        return pd.DataFrame()  # Devolver un DataFrame vacío si el horario está vacío
    df_horario = pd.DataFrame(horario)
    filas = []
    for i in range(0, len(df_horario), 5):
        filas.append(df_horario.iloc[i:i+5])
        filas.append(pd.DataFrame([[''] * len(df_horario.columns)], columns=df_horario.columns))
    df_horario = pd.concat(filas, ignore_index=True)
    return df_horario

# Crear un DataFrame para almacenar todos los horarios
df_horarios = pd.DataFrame()
for i, horario in enumerate(horarios):
    df_horario = agregar_fila_vacia(horario)
    if not df_horario.empty:  # Verificar que el DataFrame no esté vacío
        df_horario['Horario'] = i + 1  # Agregar una columna para identificar el horario
        df_horarios = pd.concat([df_horarios, df_horario], ignore_index=True)

# Guardar los horarios generados en un archivo CSV
df_horarios.to_csv(r'D:\Programacion\Python\Practica\Codedex\Python_intermediate\horarios_generados.csv', index=False)

print("10 horarios generados y guardados exitosamente.")
