import unittest
from grain import Grain

class TestGrain(unittest.TestCase):
    def test_is_valid(self):
        valid_grain = Grain()
        valid_grain.origine = "Vietnam"
        valid_grain.arome = "Floral"
        valid_grain.annee = 2017
        valid_grain.corps = 5
        self.assertTrue(valid_grain.is_valid())

        invalid_grain = Grain()
        invalid_grain.origine = "france"
        invalid_grain.arome = "Fruite"
        invalid_grain.annee = 2022
        invalid_grain.corps = 10
        self.assertFalse(invalid_grain.is_valid())

if __name__ == '__main__':
    unittest.main()
