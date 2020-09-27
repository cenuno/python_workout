"""
Author:         Cristian Nuno
Date:           September 27, 2020
Exercise 09:    First-last
"""

from typing import List, Sequence, Tuple, TypeVar

GeneralSeq = TypeVar("GeneralSeq", List[int], str, Tuple[int])


def firstlast(x: GeneralSeq) -> Sequence:
    """
    Find the first and last elements from a given sequence.

    Args:
        x (GeneralSeq): a sequence (list, string, or tuple)

    Returns:
        sequence: two-element sequence of the same type as x

    Examples:
        >>> firstlast("abc")
        'ac'

        >>> firstlast([1, 2, 3, 4])
        [1, 4]

        >>> firstlast((4, 55, 3))
        (4, 3)
    """
    # find the first and last element and preserve each element's parent type
    first = x[0:1]
    last = x[-1:]

    # return the concatenated form of the two elements together
    return first + last


if __name__ == "__main__":
    import doctest
    doctest.testmod()
