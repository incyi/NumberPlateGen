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

def random_string(length, chars):
    """Generates a random string of a specified length from given characters."""
    return ''.join(random.choice(chars) for _ in range(length))

def random_digits(length):
    """Generates a random string of digits of a specified length."""
    return random_string(length, '0123456789')

def random_letters(length):
    """Generates a random string of uppercase letters of a specified length."""
    return random_string(length, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
