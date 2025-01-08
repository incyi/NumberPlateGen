from ..utils import random_letters, random_digits  # Updated import

# https://www.gov.uk/displaying-number-plates

def uk_plate_format():
    """Generates a random UK number plate."""
    return f"{random_letters(2)} {random_digits(2)} {random_letters(3)}"
