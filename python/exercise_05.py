"""
Author:         Cristian Nuno
Date:           September 14, 2020
Exercise 05:    Pig Latin
"""


def pig_latin(word: str) -> str:
    """
    Translate any word into pig latin.

    If the word begins with a vowel (a, e, i, o, or u),
    add “way” to the end of the word.

    If the word begins with any other letter, place first letter
    at the end of the word and then add “ay.”

    Args:
        word (string): a word

    Returns:
        str: the word translated into pig latin

    Examples:
        >>> pig_latin("tree")
        'reetay'

        >>> pig_latin("air")
        'airway'

        >>> pig_latin("eat")
        'eatway'

        >>> pig_latin("python")
        'ythonpay'

        >>> pig_latin("computer")
        'omputercay'
    """
    # store constants
    VOWELS = ["a", "e", "i", "o", "u"]
    WAY = 'way'
    AY = 'ay'

    if word[0] in VOWELS:
        translation = word + WAY
    else:
        translation = word[1:] + word[0] + AY

    return translation


if __name__ == "__main__":
    import doctest
    doctest.testmod()
