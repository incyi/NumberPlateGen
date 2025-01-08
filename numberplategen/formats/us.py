from ..utils import random_letters, random_digits  # Updated import

def us_plate_format():
    """Generates a random US license plate."""
    return f"{random_digits(1)}{random_letters(3)}{random_digits(3)}"
