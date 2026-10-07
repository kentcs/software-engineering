"""Retrieve Wikipedia HTML without parsing it or opening a browser."""
import requests

URL = "https://en.wikipedia.org/wiki/Selenium_(software)"
HEADERS = {"User-Agent": "SoftwareEngineeringCourse/1.0 (educational example)"}


def test_wikipedia_response():
    response = requests.get(URL, headers=HEADERS, timeout=15)
    assert response.status_code == 200, response.status_code
    assert "text/html" in response.headers["Content-Type"]
    assert "Selenium_WebDriver" in response.text
    print("HTTP status:", response.status_code)
    print(response.text[:500])


def main():
    test_wikipedia_response()


if __name__ == "__main__":
    main()
