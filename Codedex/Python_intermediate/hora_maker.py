import pandas as pd

# Ruta del archivo CSV
ruta_csv = 'D:\\Programacion\\Python\\Practica\\Codedex\\Python_intermediate\\Horarios.csv'

# Leer el archivo CSV
df = pd.read_csv(ruta_csv)

# Eliminar espacios en blanco de los nombres de las columnas
df.columns = df.columns.str.strip()

# Imprimir las columnas y las primeras filas del DataFrame para ver su contenido
print("Columnas del DataFrame:")
print(df.columns)
print("\nPrimeras filas del DataFrame:")
print(df.head())

# Convertir las horas a un formato manejable
def limpiar_hora(hora_str):
    if pd.isna(hora_str) or hora_str.strip() == "NO" or isinstance(hora_str, str) and hora_str.strip().isalpha():
        return None
    try:
        h, m = map(int, hora_str.strip().split(':'))
        return h * 60 + m
    except ValueError:
        return None

# Aplicar la limpieza a las columnas de horas
for dia in ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']:
    if dia in df.columns and f'{dia}-end' in df.columns:
        df[f'{dia}_start'] = df[dia].apply(limpiar_hora)
        df[f'{dia}_end'] = df[f'{dia}-end'].apply(limpiar_hora)

# Eliminar filas duplicadas basadas en las columnas 'Maestro' y 'Materia'
df = df.drop_duplicates(subset=['Maestro', 'Materia'])

# Función para verificar si dos intervalos de tiempo se solapan
def solapan(hora_inicio1, hora_fin1, hora_inicio2, hora_fin2):
    return not (hora_fin1 <= hora_inicio2 or hora_fin2 <= hora_inicio1)

# Función para generar un horario sin repetir materias y sin solapamientos
def generar_horario(df):
    horario = []
    materias_agregadas = set()
    df_shuffled = df.sample(frac=1).reset_index(drop=True)  # Mezclar el DataFrame
    maestros = df_shuffled['Maestro'].unique()
    for maestro in maestros:
        clases_maestro = df_shuffled[df_shuffled['Maestro'] == maestro]
        for index, clase in clases_maestro.iterrows():
            if clase['Materia'] not in materias_agregadas:
                # Verificar que no haya solapamientos en el horario
                conflicto = False
                for dia in ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']:
                    if f'{dia}_start' in clase and f'{dia}_end' in clase:
                        hora_inicio = clase[f'{dia}_start']
                        hora_fin = clase[f'{dia}_end']
                        for otra_clase in horario:
                            otra_hora_inicio = otra_clase[f'{dia}_start']
                            otra_hora_fin = otra_clase[f'{dia}_end']
                            if otra_hora_inicio is not None and otra_hora_fin is not None and hora_inicio is not None and hora_fin is not None:
                                if solapan(hora_inicio, hora_fin, otra_hora_inicio, otra_hora_fin):
                                    conflicto = True
                                    break
                    if conflicto:
                        break
                
                if not conflicto:
                    horario.append(clase)
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
df_horarios.to_csv('D:\\Programacion\\Python\\Practica\\Codedex\\Python_intermediate\\horarios_generados.csv', index=False)

print("10 horarios generados y guardados exitosamente.")