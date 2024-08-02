def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    grade_thresholds = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
    }
    
    # Calcular el rango de puntuación para cada intervalo
    range_per_grade = (highest - 40) / 4
    
    # Definir los umbrales
    grade_thresholds["D"] = 41
    grade_thresholds["C"] = grade_thresholds["D"] + range_per_grade
    grade_thresholds["B"] = grade_thresholds["C"] + range_per_grade
    grade_thresholds["A"] = grade_thresholds["B"] + range_per_grade
    
    # Redondear los umbrales
    for grade in grade_thresholds:
        grade_thresholds[grade] = round(grade_thresholds[grade])
    
    return grade_thresholds

# Test cases
print(letter_grades(100))  # {'A': 86, 'B': 71, 'C': 56, 'D': 41}