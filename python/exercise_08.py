"""
Author:         Cristian Nuno
Date:           September 27, 2020
Exercise 08:    Sorting a string
"""


def strsort(word: str) -> str:
    """
    Sort the characters in a word from the lowest to the highest Unicode value.

    Args:
        word (str): a word

    Returns:
        str: the rearranged word with its characters sorted from the
             lowest to the highest Unicode value.

    Examples:
        >>> strsort("cba")
        'abc'
    """
    # use sorted() to sort each character in ascending order of Unicode value
    output = sorted(word)

    # return the list of characters together as a string
    return "".join(output)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
