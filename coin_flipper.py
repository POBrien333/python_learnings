# COIN FLIP SIMULATOR
# Code that simulates flipping a single coin however many times the user decides.
# The code should record the outcomes and count the number of tails and heads.

import random
headntail = ['heads','tails']
heads = 0
tails = 0

# Coin Flip function (include counter)
def coin_flipper():
    return random.choice(headntail)


# Input from user asking if they want to flip a coin
while True:

    answer = input("Do you want to flip a coin? Enter 'y' or 'n' ")
    if answer[0].lower() == 'y':
        flip = coin_flipper()
        if flip == 'heads':
            heads += 1
            print("You got HEADS")
        else:
            tails += 1
            print("You got TAILS")

    else:
        print("Thanks for flipping!")
        print("A total of ", str(heads), 'heads and', str(tails), "tails was counted")
        break
