"""This module provides the NL (The Netherlands) number plate formats.

It includes functions for generating various NL number plate patterns.
"""
import random  # Standard library import
from ..utils import random_letters, random_digits  # Local import

# https://www.rdw.nl/particulier/voertuigen/auto/de-kentekenplaat/cijfers-en-letters-op-de-kentekenplaat
# Ingangsdatum kentekenserie 	 Serie 	 Combinatie
# 20-01-2000	6 	            99-XX-XX
# 19-05-2008 	7 	            99-XXX-9
# 05-03-2013 	8 	            9-XXX-99
# 30-03-2015 	9 	            XX-999-X
# 19-08-2019 	10 	            X-999-XX
# 04-06-2024 	11              XXX-99-X

def nl_plate_format():
    """Generates a random NL number plate using various formats."""

    # List of different formats
    formats = [
        f"{random_digits(2)}-{random_letters(2)}-{random_letters(2)}",  # 99-XX-XX
        f"{random_digits(2)}-{random_letters(3)}-{random_digits(1)}",  # 99-XXX-9
        f"{random_digits(1)}-{random_letters(3)}-{random_digits(2)}",  # 9-XXX-99
        f"{random_letters(2)}-{random_digits(3)}-{random_letters(1)}",  # XX-999-X
        f"{random_digits(1)}-{random_digits(3)}-{random_letters(2)}",  # X-999-XX
        f"{random_letters(3)}-{random_digits(2)}-{random_letters(1)}"  # XXX-99-X
    ]

    # Randomly select one of the formats
    selected_format = random.choice(formats)
    return selected_format
