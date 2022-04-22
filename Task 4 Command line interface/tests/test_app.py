import unittest
from unittest.mock import patch, mock_open
from myapp import unique_characters, parse_input, parser


class TestClass(unittest.TestCase):
    def test_unique_characters(self):
        self.param_list = [("abbabcde", 3), ("dkfppplllere", 4), ("ttppllffhgyyyy", 2)]
        for p1, p2 in self.param_list:
            with self.subTest(p1=p2):
                self.assertEqual(unique_characters(p1), p2)
        self.assertRaises(TypeError, unique_characters, 12345)

    @patch("myapp.app.open", new_callable=mock_open, read_data="iuhu")
    def test_parse_input(self, mocked_open):
        result = parse_input(parser.parse_args(["--file", "mock\\path"]))
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
