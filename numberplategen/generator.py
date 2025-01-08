"""Generator for creating random number plate formats.

This module provides functionality for generating random number plates
in various formats, including formats for different countries. It includes
utility functions for generating random letters and digits, which are used
to construct valid number plate strings based on specified patterns.

Functions:
- random_letters(length): Generates a string of random uppercase letters.
- random_digits(length): Generates a string of random digits.
- nl_plate_format(): Generates a random NL number plate.
"""

import random
from .formats import supported_formats
from .utils import random_digits, random_letters  # Updated import

def generate_number_plate(region):
    """
    Generates a random number plate based on the specified region.

    :param region: The region code (e.g., 'us', 'uk', 'india').
    :return: A randomly generated number plate string.
    :raises ValueError: If the region is not supported.
    """
    if region not in supported_formats:
        raise ValueError(f"Region '{region}' not supported. Please choose from {list(supported_formats.keys())}.")

    # Get the plate format function for the specified region
    format_function = supported_formats[region]

    # Generate the number plate using the format function
    return format_function()

def random_letters(length):
    """Generates a string of random uppercase letters."""
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=length))

def random_digits(length):
    """Generates a string of random digits."""
    return ''.join(random.choices('0123456789', k=length))

def nl_plate_format():
    """Generates a random NL number plate."""
    formats = [
        f"{random_digits(2)}-{random_letters(2)}-{random_letters(2)}",  # 99-XX-XX
        f"{random_digits(2)}-{random_letters(3)}-{random_digits(1)}",   # 99-XXX-9
        f"{random_digits(1)}-{random_letters(3)}-{random_digits(2)}",   # 9-XXX-99
        f"{random_letters(2)}-{random_digits(3)}-{random_letters(1)}",  # XX-999-X
        f"{random_digits(1)}-{random_digits(3)}-{random_letters(2)}",   # X-999-XX
        f"{random_letters(3)}-{random_digits(2)}-{random_letters(1)}",  # XXX-99-X
    ]
    return random.choice(formats)
