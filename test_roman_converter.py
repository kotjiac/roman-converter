import unittest
from roman_converter import roman_to_int

class TestRomanToInt(unittest.TestCase):
    
    def test_basic_numerals(self):
        self.assertEqual(roman_to_int("I"), 1)
        self.assertEqual(roman_to_int("V"), 5)
        self.assertEqual(roman_to_int("X"), 10)
        self.assertEqual(roman_to_int("L"), 50)
        self.assertEqual(roman_to_int("C"), 100)
        self.assertEqual(roman_to_int("D"), 500)
        self.assertEqual(roman_to_int("M"), 1000)
    
    def test_valid_combinations(self):
        self.assertEqual(roman_to_int("II"), 2)
        self.assertEqual(roman_to_int("IV"), 4)
        self.assertEqual(roman_to_int("IX"), 9)
        self.assertEqual(roman_to_int("XII"), 12)
        self.assertEqual(roman_to_int("XXI"), 21)
        self.assertEqual(roman_to_int("XL"), 40)
        self.assertEqual(roman_to_int("XC"), 90)
        self.assertEqual(roman_to_int("C"), 100)
        self.assertEqual(roman_to_int("CD"), 400)
        self.assertEqual(roman_to_int("D"), 500)
        self.assertEqual(roman_to_int("CM"), 900)
        self.assertEqual(roman_to_int("M"), 1000)
        self.assertEqual(roman_to_int("MCMXCIV"), 1994)
    
    def test_boundary_values(self):
        self.assertEqual(roman_to_int("I"), 1)
        self.assertEqual(roman_to_int("MMMCMXCIX"), 3999)
    
    def test_invalid_numerals(self):
        with self.assertRaises(ValueError):
            roman_to_int("IIII")
        with self.assertRaises(ValueError):
            roman_to_int("VV")
        with self.assertRaises(ValueError):
            roman_to_int("IIIV")
        with self.assertRaises(ValueError):
            roman_to_int("IC")
        with self.assertRaises(ValueError):
            roman_to_int("IM")
        with self.assertRaises(ValueError):
            roman_to_int("VX")
        with self.assertRaises(ValueError):
            roman_to_int("MCMXCIVI")
        with self.assertRaises(ValueError):
            roman_to_int(" ")
        with self.assertRaises(ValueError):
            roman_to_int("123")
        with self.assertRaises(ValueError):
            roman_to_int("ABCD")
    
    def test_mixed_invalid_numerals(self):
        with self.assertRaises(ValueError):
            roman_to_int("XAI")
        with self.assertRaises(ValueError):
            roman_to_int("MIIM")
    
if __name__ == '__main__':
    unittest.main()