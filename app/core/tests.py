"""
Sample tests
"""

from django.test import SimpleTestCase

from core import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_sub_numbers(self):
        """Test subtracting numbers from each other."""
        res = calc.sub(1, 10)
        self.assertEqual(res, -9)
