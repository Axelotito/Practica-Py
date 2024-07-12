""" fizz buzz game """
for num in range(1, 101):
    residuo1 = num % 3
    residuo2 = num % 5

    if residuo1 == 0 and residuo2 == 0:
        print('FizzBuzz')
    elif residuo1 == 0:
        print('Fizz')
    elif residuo2 == 0:
        print('Buzz')
    else:
        print(num)
