import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Selenium_(software)"
HEADERS = {"User-Agent": "SoftwareEngineeringCourse/1.0 (educational example)"}


def test_wikipedia_html():
    response = requests.get(URL, headers=HEADERS, timeout=15)
    assert response.status_code == 200, response.status_code
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("h1")
    assert title is not None
    assert title.get_text(strip=True) == "Selenium (software)"
    heading = soup.find(id="Selenium_WebDriver")
    assert heading is not None
    paragraph = heading.find_next("p")
    assert paragraph is not None
    text = paragraph.get_text(" ", strip=True)
    assert "WebDriver" in text
    print(text)
    link = paragraph.find("a")
    assert link is not None
    print("First link:", link.get_text(" ", strip=True))
    print("Destination:", link.get("href"))


def main():
    test_wikipedia_html()


if __name__ == "__main__":
    main()
