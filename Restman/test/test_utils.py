import unittest
from src.utils import parse_json_string

class TestUtils(unittest.TestCase):

    def test_parse_json_string_valid(self):
        result = parse_json_string('{"key": "value"}')
        self.assertEqual(result, {"key": "value"})

    def test_parse_json_string_invalid(self):
        with self.assertRaises(ValueError):
            parse_json_string('Invalid JSON')

if __name__ == '__main__':
    unittest.main()
