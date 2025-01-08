# numberplategen/utils.py
import random

def random_letters(length):
    """Generates a string of random uppercase letters."""
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=length))

def random_digits(length):
    """Generates a string of random digits."""
    return ''.join(random.choices('0123456789', k=length))
