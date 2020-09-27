"""
Author:         Cristian Nuno
Date:           September 27, 2020
Exercise 10:    Summing Anything
"""

from typing import List, Sequence, TypeVar

GeneralSeq = TypeVar("GeneralSeq", List[int], str)


def mysum(*sequences: GeneralSeq) -> Sequence:
    """
    Recreate the built-in sum() function.

    Rather than a list of sequences, as the sole parameter,
    mysum() takes individual sequences as parameters and then returns the sum.

    Args:
        *numbers: a series of sequences, separated by a comma

    Returns:
        Sequence: the sum of the series of sequences

    Examples:
        >>> mysum(1, 2, 3, 4)
        10

        >>> mysum(1.2, 3.4, 5.6)
        10.2

        >>> mysum("abc", "def")
        'abcdef'

        >>> mysum([1,2,3], [4,5,6])
        [1, 2, 3, 4, 5, 6]

        >>> mysum((10, 20, 30), (40, 50, 60))
        (10, 20, 30, 40, 50, 60)
    """
    # if nothing given, return nothing
    if not sequences:
        return sequences

    # otherwise, store the first sequence
    output = sequences[0]
    # for all other sequences, sum them onto the first sequence
    for seq in sequences[1:]:
        output += seq
    return output


if __name__ == "__main__":
    import doctest
    doctest.testmod()
