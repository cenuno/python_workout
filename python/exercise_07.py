"""
Author:         Cristian Nuno
Date:           September 16, 2020
Exercise 07:    Ubbi Dubbi
"""


def ubbi_dubbi(word: str) -> str:
    """
    Translate each word to Ubbi Dubbi.

    In Ubbi Dubbi, every vowel (a, e, i, o, or u) is prefaced with ub.
    In theory, you only put an ub before every vowel sound,
    rather than before each vowel.

    Args:
        word (str): a word

    Returns:
        str: a word translated into Ubbi Dubbi

    Examples:
        >>> ubbi_dubbi("milk")
        'mubilk'

        >>> ubbi_dubbi("program")
        'prubogrubam'

        >>> ubbi_dubbi("aardvark")
        'ubaubardvubark'
    """
    # store constants
    VOWELS = 'aeiou'
    UB = 'ub'

    # store new words
    translation = []

    # for each character, add the "UB" prefix to characters that are vowels
    for char in word:
        if char in VOWELS:
            translation.append(UB + char)
        else:
            translation.append(char)

    # return the translated version of the word
    return "".join(translation)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
