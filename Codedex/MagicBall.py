""" Make a magic 8 ball that will respond to a user's question. """
import random 

question = input("Ask the magic 8 ball a question: ")

number = random.randint(1,9)

if number == 1:
    print("Yes - definitely.")
elif number == 2: 
    print('It is decidedly so.')
elif number == 3: 
    print('Without a doubt.')
elif number == 4: 
    print('Reply hazy, try again.')
elif number == 5: 
    print('Ask again later.')
elif number == 6:
    print('Better not tell you now.')
elif number == 7:
    print('My sources say no.')
elif number == 8:
    print('Outlook not so good.')
elif number == 9:
    print('Very doubtful.')

# The code above is a magic 8 ball that will respond to a user's question.