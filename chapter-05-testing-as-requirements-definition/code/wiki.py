"""Fetch the text of a Wikipedia page."""
import requests

HEADERS = {"User-Agent": "SoftwareEngineeringCourse/1.0 (educational example)"}


def page_text(title):
    url = "https://en.wikipedia.org/wiki/" + title
    response = requests.get(url, headers=HEADERS, timeout=15)
    response.raise_for_status()
    return response.text
