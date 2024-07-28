import pandas as pd

# Leer el archivo CSV desde la ruta especificada
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

# Función para generar un horario
def generar_horario(df):
    horario = []
    maestros = df['Maestro'].unique()
    for maestro in maestros:
        clases_maestro = df[df['Maestro'] == maestro]
        clases_seleccionadas = clases_maestro.sample(n=min(3, len(clases_maestro)))
        for index, clase in clases_seleccionadas.iterrows():
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
    return horario

# Generar los horarios
horario1 = generar_horario(df)
horario2 = generar_horario(df)
horario3 = generar_horario(df)

# Convertir los horarios a DataFrame y agregar una fila vacía después de cada 5 materias
def agregar_fila_vacia(horario):
    df_horario = pd.DataFrame(horario)
    filas = []
    for i in range(0, len(df_horario), 5):
        filas.append(df_horario.iloc[i:i+5])
        filas.append(pd.DataFrame([[''] * len(df_horario.columns)], columns=df_horario.columns))
    df_horario = pd.concat(filas, ignore_index=True)
    return df_horario

df_horario1 = agregar_fila_vacia(horario1)
df_horario2 = agregar_fila_vacia(horario2)
df_horario3 = agregar_fila_vacia(horario3)

# Guardar los horarios generados en archivos CSV
df_horario1.to_csv(r'D:\Programacion\Python\Practica\Codedex\Python_intermediate\horario1.csv', index=False)
df_horario2.to_csv(r'D:\Programacion\Python\Practica\Codedex\Python_intermediate\horario2.csv', index=False)
df_horario3.to_csv(r'D:\Programacion\Python\Practica\Codedex\Python_intermediate\horario3.csv', index=False)

print("Horarios generados y guardados exitosamente.")