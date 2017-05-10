import lxml
import os
import unittest
import solve_puzzle 


class TestOperations(unittest.TestCase):
    def setUp(self):
        self.html_filename = os.path.join(
            os.path.dirname(__file__),
            "example.html",
        )

    def test_parse_html(self):
        elem = solve_puzzle.parse_html(self.html_filename)
        self.assertIsInstance(
            elem,
            lxml.html.HtmlElement,
        )

    def test_count_filled_images(self):
        elem = solve_puzzle.parse_html(self.html_filename)
        # Based on the sample html we know there is 49 filled dots.
        self.assertEqual(
            49,
            solve_puzzle.count_filled_images(elem),
        )
