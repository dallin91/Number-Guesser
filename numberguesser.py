# This program is a small number guessing game
# Created by: Dallin Reeves
# April 8, 2019 7:01PM

import random

min = 0
max = 100

num = random.randint(min, max)

guess = int(input('Guess a number between 0 and 100: '))

while guess != num:
    if guess > num:
        print('Too high!')
    else:
        print('Too low!')
    guess = int(input('Guess again! '))

print('YEEHAW! You did it!')