"""
Dice file.
Create dice of N size.
Roll dice. Hold returned roll
Return roll
"""

import random


def roll_dice(user_size):
    """
    Creates dice of N size
    :param: user_size: user chosen size
    :return: roll: random number from dice
    """
    dice = range(1, user_size+1)
    roll = random.choice(dice)
    return roll


def ask_user():
    """
    Main loop. Asks user for input, calls roll_dice
    :return:
    """
    while 1:
        dice_size = int(raw_input("Hello, please choose a size for your dice.\n" ))
        roll = roll_dice(dice_size)
        print "You rolled", roll


ask_user()
