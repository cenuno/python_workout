"""
Author:         Cristian Nuno
Date:           September 8, 2020
Exercise 01:    Number Guessing Game
"""

import random


# create the Number Guessing Game function
def guessing_game():
    """
    Prompt the user to a guess a number between 0 and 100 (inclusive).
    If guess is correct, the program exists; otherwise they'll try again.
    """
    random_int = random.randint(0, 100)

    start_text = """
    === It's time to play the 'Guessing Game'! ===

    Here are the rules: guess a number between 0 and 100 (inclusive).
    Once you have your guess enter it into the computer.
    Even if you get it wrong, the game won't end until you get it right!

    Shake off the nerves and play the 'Guessing Game'!

    > """

    guess_int = int(input(start_text))

    while True:
        if guess_int < random_int:
            guess_int = int(input("Too low, try a higher number!\n> "))
        elif guess_int > random_int:
            guess_int = int(input("Too high, try a lower number!\n> "))
        else:
            print("Just right! You have won the 'Guessing Game'!\n")
            break


# call the function
guessing_game()
