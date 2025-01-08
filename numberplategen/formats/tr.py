from ..utils import random_letters, random_digits  # Updated import

def tr_plate_format():
    """Generates a random NL number plate."""
    return f"{random_digits(2)} {random_letters(3)} {random_digits(2)}"
