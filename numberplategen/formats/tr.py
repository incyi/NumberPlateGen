"""This module provides the TR (Turkiye) number plate formats.

It includes functions for generating various TR number plate patterns.
"""

from ..generator import random_letters, random_digits  # Local import

def tr_plate_format():
    """Generates a random NL number plate."""
    return f"{random_digits(2)} {random_letters(3)} {random_digits(2)}"
