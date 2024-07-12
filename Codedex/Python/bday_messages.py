import random
def birthday_message():
    list = [
        'Hope you have a great day!',
        'It\'s your special day! - get out there and enjoy it!',
        'Yuo were born and the world got better! - everyone wins!',
        'Have lots of fun on your especial day!',
        'Anoter year of you going around the sun!'
    ]
    random_message = random.choice(list)
    return random_message