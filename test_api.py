import unittest
import requests
import json

# Define the base URL for the API
BASE_URL = "http://127.0.0.1:5000"

class TestRomanApi(unittest.TestCase):

    def test_valid_roman_mcmlxxxi(self):
        response = requests.get(f"{BASE_URL}/romantointeger/MCMLXXXI")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"integer": 1981}) # Corrected expected value

    def test_valid_roman_iv(self):
        response = requests.get(f"{BASE_URL}/romantointeger/IV")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"integer": 4})

    def test_invalid_roman_input(self):
        response = requests.get(f"{BASE_URL}/romantointeger/INVALID")
        self.assertEqual(response.status_code, 400)
        # We expect a specific error structure, but the details message can vary.
        # So, we check for the presence of "error" and its value.
        response_data = response.json()
        self.assertIn("error", response_data)
        self.assertEqual(response_data["error"], "Invalid Roman numeral")
        self.assertIn("details", response_data) # Check if 'details' key is present

    def test_edge_case_smallest_valid(self):
        response = requests.get(f"{BASE_URL}/romantointeger/I")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"integer": 1})

    def test_edge_case_largest_valid(self):
        response = requests.get(f"{BASE_URL}/romantointeger/MMMCMXCIX")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"integer": 3999})

    def test_valid_roman_mmxxi(self): # Added from original description, target was MCMLXXXI -> 1981
        response = requests.get(f"{BASE_URL}/romantointeger/MMXXI")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"integer": 2021})

    def test_valid_roman_mcmxciv(self): # Added to match original description for 1994
        response = requests.get(f"{BASE_URL}/romantointeger/MCMXCIV")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"integer": 1994})


if __name__ == '__main__':
    # Note: For these tests to run, the Flask app (app.py) must be running separately.
    # You can run the app using `python app.py` in one terminal,
    # and then run these tests using `python -m unittest test_api.py` in another.
    unittest.main()
