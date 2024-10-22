import unittest
from unittest.mock import patch, MagicMock
from src.restman import Restman

class TestRestman(unittest.TestCase):

    # Under the project folder Restman, run the following command: 
    # python -m unittest test.test_restman.TestRestman.test_get_success
    @patch('requests.get')
    def test_get_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = '{"message": "success"}'
        mock_get.return_value = mock_response

        restman = Restman()
        response = restman.get('https://catfact.ninja/fact', headers=None, cert=None, timeout=5)

        mock_get.assert_called_once_with('https://catfact.ninja/fact', headers=None, cert=None, timeout=5)
        self.assertEqual(response.text, '{"message": "success"}')

    @patch('requests.post')
    def test_post_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.text = '{"message": "posted"}'
        mock_post.return_value = mock_response

        restman = Restman()
        response = restman.post('http://example.com', headers=None, data='{"key": "value"}', cert=None, timeout=5)

        mock_post.assert_called_once_with('http://example.com', headers=None, json={'key': 'value'}, cert=None, timeout=5)
        self.assertEqual(response.text, '{"message": "posted"}')

    def test_invalid_headers(self):
        restman = Restman()
        with self.assertRaises(ValueError):
            restman._parse_headers("Invalid JSON string")

if __name__ == '__main__':
    unittest.main()
