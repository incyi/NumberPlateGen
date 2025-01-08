"""This module provides the UK (The United Kingdom) number plate formats.

It includes functions for generating various UK number plate patterns.
"""

from ..utils import random_letters, random_digits  # Local import

# https://www.gov.uk/displaying-number-plates

def uk_plate_format():
    """Generates a random UK number plate."""
    return f"{random_letters(2)} {random_digits(2)} {random_letters(3)}"
