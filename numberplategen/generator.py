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

from .formats import supported_formats

def generate_number_plate(region):
    """
    Generates a random number plate based on the specified region.

    :param region: The region code (e.g., 'us', 'uk', 'india').
    :return: A randomly generated number plate string.
    :raises ValueError: If the region is not supported.
    """
    if region not in supported_formats:
        raise ValueError(f"Region '{region}' not supported. Use: {list(supported_formats.keys())}.")

    # Get the plate format function for the specified region
    format_function = supported_formats[region]

    # Generate the number plate using the format function
    return format_function()
