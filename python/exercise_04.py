"""
Author:         Cristian Nuno
Date:           September 12, 2020
Exercise 04:    Hexadecimal Output
"""


def hex_output(hex_number: str) -> int:
    """
    Return the integer form of a hexadecimal number without the 0x prefix.

    Background:
        In mathematics and computing, hexadecimal (also base 16, or hex) is a
        positional system that represents numbers using a base of 16.
        Unlike the common way of representing numbers with ten symbols,
        it uses sixteen distinct symbols.

    Args:
        hex_number (string): a hexadecimal number without the 0x prefix

    Returns:
        int: the integer equivalent of the hexadecimal input

    Examples:
        >>> hex_output('50')
        80

        >>> hex_output('4d2')
        1234

        >>> hex_output('ce0a6d74')
        3456789876
    """
    output = 0
    # reverse the digits within the hex_number and
    # obtain both the index and individual digit.
    for power, digit in enumerate(reversed(hex_number)):
        # convert each digit into an integer,
        # multiply it by 16 raised to the index, and
        # add the product into the output
        output += int(digit, base=16) * (16 ** power)
    return output


if __name__ == "__main__":
    import doctest
    doctest.testmod()
