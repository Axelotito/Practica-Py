import pandas as pd

# Read the CSV file
df = pd.read_csv('D:\\Programacion\\Python\\Practica\\Codedex\\Python_intermediate\\HORICO2025-I.xlsx - Consulta1.csv')

# Strip spaces from column names
df.columns = df.columns.str.strip()

# Print the columns to debug
print("Columns in DataFrame:", df.columns)

# Mapping of start and end time columns
time_columns = {
    'Lunes': ('Lunes', ''),
    'Martes': ('Martes', '.1'),
    'Miercoles': ('Miercoles', '.2'),
    'Jueves': ('Jueves', '.3'),
    'Viernes': ('Viernes', '.4')
}

# Function to parse time strings into tuples of (start, end)
def parse_time(row, day):
    start_col, end_col = time_columns[day]
    start_time = row[start_col]
    end_time = row[end_col]
    if pd.notna(start_time) and pd.notna(end_time):
        return (start_time, end_time)
    return None

# Function to check if two time intervals overlap
def times_overlap(time1, time2):
    if time1 is None or time2 is None:
        return False
    start1, end1 = time1
    start2, end2 = time2
    return not (end1 <= start2 or end2 <= start1)

# Function to check if a subject can be added to a schedule without overlapping
def can_add_subject(schedule, subject):
    for day in time_columns.keys():
        new_time = parse_time(subject, day)
        for existing_subject in schedule:
            existing_time = parse_time(existing_subject, day)
            if times_overlap(new_time, existing_time):
                return False
    return True

# Function to create non-overlapping schedules
def create_schedules(df):
    schedules = [[], [], []]
    for _, subject in df.iterrows():
        for schedule in schedules:
            if can_add_subject(schedule, subject):
                schedule.append(subject)
                break
    return schedules

# Create the schedules
schedules = create_schedules(df)

# Print the schedules
for i, schedule in enumerate(schedules):
    print(f"Schedule {i+1}:")
    for subject in schedule:
        print(subject['Materia'], subject['Profesor'], subject['Grupo'])
    print()