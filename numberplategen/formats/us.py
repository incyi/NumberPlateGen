"""This module provides the US (The United States of America) number plate formats.

It includes functions for generating various US number plate patterns.
"""

from ..utils import random_letters, random_digits  # Local import

def us_plate_format():
    """Generates a random US license plate."""
    return f"{random_digits(1)}{random_letters(3)}{random_digits(3)}"
