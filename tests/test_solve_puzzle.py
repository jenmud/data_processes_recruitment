import lxml
import os
import unittest
import solve_puzzle
import mock


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

    @mock.patch("solve_puzzle.requests.post")
    def test_solve_puzzle(self, mock_post):
        solve_puzzle.solve_puzzle(self.html_filename, 1234)
        mock_post.assert_called_once_with(
            self.html_filename,
            {
                "jobref": 1234,
                "valuee": 49,  # 49 filled in the sample data
            }
        )
        
