"""
Deck isn't currently unit-tested.

This is wrong: if you have time for this, don't hesistate to fork and file a pull request ;)
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
