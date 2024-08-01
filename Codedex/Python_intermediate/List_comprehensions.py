# Write code below 💖

numbers_1 = [1, 2, 3, 4, 5]
squares = []

for num in numbers_1:
    squares.append(num**2)

""" there is another way to make this """

squared_numbers = [num**2 for num in numbers_1]

print("original numbers:", numbers_1)
print("Squared numbers:", squared_numbers)
print("Squared numbers:", squares)

""" excercise """
numbers_2 = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]


def numbers_even(number):
    return (number % 2) == 0


even_numbers = [num for num in numbers_2 if num % 2 == 0]

print("Even numbers:", even_numbers)
