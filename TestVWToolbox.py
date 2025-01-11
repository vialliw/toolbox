import unittest
from unittest.mock import patch
from vw_toolbox import convert_list_to_a_string, ask_user_input_num, ask_user_input_int

class TestVWToolbox(unittest.TestCase):
    """Unit tests for the vw_toolbox module."""

    def test_convert_list_to_a_string(self):
        """Test convert_list_to_a_string function."""
        self.assertEqual(convert_list_to_a_string(['Hello', 'world'], ' '), 'Hello world')
        self.assertEqual(convert_list_to_a_string(['1', '2', '3'], ','), '1,2,3')
        self.assertEqual(convert_list_to_a_string([], ','), '')

    @patch('builtins.input', side_effect=['42'])
    def test_ask_user_input_int_valid(self, mock_input):
        """Test ask_user_input_int with valid input."""
        self.assertEqual(ask_user_input_int("Enter a number: "), 42)

    @patch('builtins.input', side_effect=['invalid', '42'])
    def test_ask_user_input_int_invalid_then_valid(self, mock_input):
        """Test ask_user_input_int with invalid input followed by valid input."""
        self.assertEqual(ask_user_input_int("Enter a number: "), 42)

    @patch('builtins.input', side_effect=['invalid', 'invalid'])
    def test_ask_user_input_int_invalid(self, mock_input):
        """Test ask_user_input_int with invalid input and error handling disabled."""
        with self.assertRaises(ValueError):
            ask_user_input_int("Enter a number: ", error_handling=False)

    @patch('builtins.input', side_effect=['42.5'])
    def test_ask_user_input_num_valid(self, mock_input):
        """Test ask_user_input_num with valid input."""
        self.assertEqual(ask_user_input_num("Enter a number: "), 42.5)

    @patch('builtins.input', side_effect=['invalid', '42.5'])
    def test_ask_user_input_num_invalid_then_valid(self, mock_input):
        """Test ask_user_input_num with invalid input followed by valid input."""
        self.assertEqual(ask_user_input_num("Enter a number: "), 42.5)

    @patch('builtins.input', side_effect=['invalid', 'invalid'])
    def test_ask_user_input_num_invalid(self, mock_input):
        """Test ask_user_input_num with invalid input and error handling disabled."""
        with self.assertRaises(ValueError):
            ask_user_input_num("Enter a number: ", error_handling=False)

if __name__ == '__main__':
    unittest.main()