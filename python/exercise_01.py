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

    Args:
        None
    Returns:
        None
    """
    answer = random.randint(0, 100)

    start_text = """
    === It's time to play the 'Guessing Game'! ===

    Here are the rules: guess a number between 0 and 100 (inclusive).
    Once you have your guess enter it into the computer.
    Even if you get it wrong, the game won't end until you get it right!

    Shake off the nerves and play the 'Guessing Game'!
    """

    print(start_text)

    while guess := int(input("> ")):
        if guess == answer:
            print(f"{guess} is just right! You won the 'Guessing Game' 🎉🥳🎉!\n")
            break
        elif guess < answer:
            print(f"{guess} is too low, try a higher number!\n")
        else:
            print(f"{guess} is too high, try a lower number!\n")


# call the function
guessing_game()
