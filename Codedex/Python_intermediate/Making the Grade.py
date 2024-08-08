"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    rounded_scores = [round(num) for num in student_scores]  # Renombrar la variable local
    return rounded_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    def conditional_fail_threshold(x):
        return x <= 40

    failed_list = filter(conditional_fail_threshold, student_scores)
    failed_list = len(list(failed_list))
    return failed_list


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    def conditional_above_threshold(x):
        return x >= threshold

    above_list = filter(conditional_above_threshold, student_scores)
    return list(above_list)


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
    number_list = []
    lowest = 40
    number_list.append(lowest + 1)  # mete 41
    result = (highest - lowest) // 4  # division entera

    for i in range(3):
        adding = number_list[i] + result
        number_list.append(adding)

    return number_list

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.
    
    :param student_scores: list - of scores in descending order.
    :param student_names: list - of names in descending order by their scores.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    ranking = []
    for i, (name, score) in enumerate(zip(student_names, student_scores), start=1):
        ranking.append(f"{i}. {name}: {score}")
    return ranking


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for student in student_info:
        if student[1] == 100:
            return student
    return []