"""Unit tests for the NumberPlateGen package.

This module contains test cases for validating the functionality
of the number plate generation.
"""

import unittest
import re
from numberplategen.formats.nl import nl_plate_format

class TestNumberPlateGen(unittest.TestCase):
    """Unit tests for the number plate generator."""

    def test_nl_plate_format(self):
        """Test the NL number plate format generation."""
        for _ in range(100):
            plate = nl_plate_format()
            # Print the plate for debugging
            print(f"Generated plate: {plate}")
            # Validate against all possible formats
            self.assertTrue(re.match(r'^\d{2}-[A-Z]{2}-[A-Z]{2}$', plate) or  # 99-XX-XX
                            re.match(r'^\d{2}-[A-Z]{3}-\d{1}$', plate) or  # 99-XXX-9
                            re.match(r'^\d{1}-[A-Z]{3}-\d{2}$', plate) or  # 9-XXX-99
                            re.match(r'^[A-Z]{2}-\d{3}-[A-Z]{1}$', plate) or  # XX-999-X
                            re.match(r'^[A-Z]{1}-\d{3}-[A-Z]{2}$', plate) or  # X-999-XX
                            re.match(r'^[A-Z]{3}-\d{2}-[A-Z]{1}$', plate))  # XXX-99-X


if __name__ == '__main__':
    unittest.main()
