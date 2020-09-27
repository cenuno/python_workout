"""
Author:         Cristian Nuno
Date:           September 10, 2020
Exercise 02:    Summing Numbers
"""


def mysum(*numbers):
    """
    Recreate the built-in sum() function.

    Rather than a list of numbers as the sole parameter,
    mysum() takes individual numbers as parameters and then returns the sum.

    Args:
        *numbers: a sequence of numbers, separated by a comma

    Returns:
        Integer or Float containing the sum from the sequence of numbers

    Examples:
        >>> mysum(1, 2, 3, 4)
        10

        >>> mysum(1.2, 3.4, 5.6)
        10.2
    """
    output = 0
    for num in numbers:
        output += num
    return output


if __name__ == "__main__":
    import doctest
    doctest.testmod()
