import unittest
from unittest.mock import Mock
from Sachet import Sachet

class TestSachet(unittest.TestCase):
    def test_is_valid(self):
        valid_sachet = Sachet()
        valid_sachet.poids = 1000
        valid_sachet.type = "pure"
        valid_sachet.grains = [Mock(is_valid=lambda: True)]
        valid_sachet.composition = [100]
        self.assertTrue(valid_sachet.is_valid(), "Valid sachet is not considered valid.")

        invalid_sachet = Sachet()
        invalid_sachet.poids = 3000
        invalid_sachet.type = "invalid"
        invalid_sachet.grains = [Mock(is_valid=lambda: True)]
        invalid_sachet.composition = [50, 50]
        self.assertFalse(invalid_sachet.is_valid(), "Invalid sachet is not considered invalid.")

if __name__ == '__main__':
    unittest.main()
