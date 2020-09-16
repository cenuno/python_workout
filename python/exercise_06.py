"""
Author:         Cristian Nuno
Date:           September 15, 2020
Exercise 06:    Pig Latin Sentence
"""

from exercise_05 import pig_latin


def pig_latin_translator(sentence: str) -> str:
    """
    Translate a series of English words into Pig Latin.

    If the word begins with a vowel (a, e, i, o, or u),
    add “way” to the end of the word.

    If the word begins with any other letter, place first letter
    at the end of the word and then add “ay.”

    Args:
        sentence (string): a sentence with each word separated by a space.

    Returns:
        str: the sentence with each word translated into pig latin

    Examples:
        >>> pig_latin_translator("this is a test translation")
        'histay isway away esttay ranslationtay'
    """
    # store each word form the sentence
    words = sentence.split()

    # create an empty list to store the pig latin translation for each word
    output = []

    # for each word, translate it to pig latin and store the results
    for word in words:
        output.append(pig_latin(word))

    # return the translated words as one sentence
    return ' '.join(output)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
