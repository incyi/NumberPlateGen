import random

def random_string(length, chars):
    """Generates a random string of a specified length from given characters."""
    return ''.join(random.choice(chars) for _ in range(length))

def random_digits(length):
    """Generates a random string of digits of a specified length."""
    return random_string(length, '0123456789')

def random_letters(length):
    """Generates a random string of uppercase letters of a specified length."""
    return random_string(length, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
