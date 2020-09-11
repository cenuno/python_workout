"""
Author:         Cristian Nuno
Date:           September 10, 2020
Exercise 02:    Summing Numbers
"""


def mysum(*numbers):
    """
    Recreate the buit-in sum() function.
    Rather than a list of numbers as the sole parameter,
    mysum() takes individual numbers as parameters and then returns the sum.
    """
    output = 0
    for num in numbers:
        output += num
    return output


# call the function
print(mysum(1, 2, 3, 4))
