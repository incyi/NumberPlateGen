"""Utility functions for generating random letters and digits.

This module provides helper functions to generate random strings of letters
and digits, which are used across various number plate generation formats.

Functions:
- random_letters(length): Generates a string of random uppercase letters.
- random_digits(length): Generates a string of random digits.
"""

import random

def random_letters(length):
    """Generates a string of random uppercase letters.

    Args:
        length (int): The number of letters to generate.

    Returns:
        str: A string of random uppercase letters.
    """
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=length))

def random_digits(length):
    """Generates a string of random digits.

    Args:
        length (int): The number of digits to generate.

    Returns:
        str: A string of random digits.
    """
    return ''.join(random.choices('0123456789', k=length))
