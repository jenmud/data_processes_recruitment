"""
The task for this problem is to find how many filled circles do you see
on the page.
"""
import argparse
import logging
from lxml import html
import requests


LOGGER = logging.getLogger(__name__)


def parse_args(): # pragma: no cover
    """
    Parse the command line args and options.

    :returns: Arguments and options.
    :rtype: :class:`argparse.Namespace`
    """
    parser = argparse.ArgumentParser(
        description="Solve Data Processors Recruitment online problems",
    )

    parser.add_argument(
        "source",
        metavar="URL",
        help="Source to parse.",
    )

    parser.add_argument(
        "--ref",
        metavar="REFERENCE",
        required=True,
        help="Job reference number",
    )

    return parser.parse_args()


def parse_html(url_filename):
    """
    Parse the HTML from URL or filename provided and returns the root
    html element.

    :param url_filename: Source being parsed.
    :type url_filename: :class:`str`
    :returns: The root element of the DOM.
    :rtype: :class:`lxml.html.HtmlElement`
    """
    return html.parse(url_filename).getroot()


def count_filled_images(elem):
    """
    Count how many image tags with a source of `filled0.gif` are found.

    :param elem: Element to iterate over for images with `filled0.gif` sources.
    :type elem: :class:`lxml.html.HtmlElement`
    :retuns: The count of found images.
    :rtype: :class:`int`
    """
    return int(elem.xpath("count(//p/img[@src='filledO.gif'])"))


def solve_puzzle(url, ref):
    """
    Fetch the puzzle and post the answer.

    :param url: Puzzle URL
    :type url: :class:`str`
    :param ref: Job reference number
    :type ref: :class:`str`
    :returns: POST response.
    :rtype: :class:`requests.Response`
    """
    elem = parse_html(url)
    total = count_filled_images(elem)
    data = {
        "title": "submit",
        "jobref": ref,
        "valuee": total,
    }
    response = requests.post(url, params=data)
    return response


if __name__ == "__main__": # pragma: no cover
    logging.basicConfig(level=logging.INFO)
    NS = parse_args()
    resp = solve_puzzle(NS.source, NS.ref) # pylint: disable=invalid-name
    LOGGER.info("Response code: %d", resp.status_code)
    LOGGER.info("Response: %s", resp.text)
