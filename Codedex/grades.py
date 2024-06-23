""" Create a grades.py program that checks whether a grade is above or below 55. """

grade = int(input("Enter your grade between 0 to 100: "))

if grade >= 55:
    print("You passed.")
    if grade >= 90:
        print("You got an A!")
    elif grade >= 80:
        print("You got a B!")
    elif grade >= 70:
        print("You got a C!")
    elif grade >= 60:
        print("You got a D!")
else:
    print("You failed.")