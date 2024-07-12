
""" GUESS THE NUMBER GAME """

guess = 0

while guess != 6:
    guess = int(input("Guess the number: "))
    if guess < 6:
        print("Too low!")
    elif guess > 6:
        print("Too high!")
        
print("You guessed it!")