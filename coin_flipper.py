'''
COIN FLIP SIMULATOR
Code that simulates flipping a single coin however many times the user decides.
The code should record the outcomes and count the number of tails and heads.'''

import random

headntail = ['heads','tails']

# Coin Flip function (include counter)
class Coins:
    def __init__(self):
        self.coincount=[]

    # Coin flip function
    def coin_flipper():
        print(random.choice(headntail))

    # Input from user asking if they want to flip a coin
while True:
    answer = input("Do you want to flip a coin? Enter 'y' or 'n' ")
    if answer[0].lower()=='y':
        flip = coin_flipper()
        coincount += flip
        print("You got: ", flip )

    else:
        print("Thanks for flipping!")
        print("A total of ", headntail.coincount('heads'), 'heads was counted')
        print("A total of ", headntail.coincount('tails'), 'tails was counted')
        break
