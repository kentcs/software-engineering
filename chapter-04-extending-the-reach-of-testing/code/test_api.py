import requests

URL = "https://api.github.com/repos/python/cpython"
HEADERS = {"Accept": "application/vnd.github+json",
           "User-Agent": "SoftwareEngineeringCourse/1.0"}


def test_repository_data():
    response = requests.get(URL, headers=HEADERS, timeout=15)
    assert response.status_code == 200, response.status_code
    repo = response.json()
    assert repo["full_name"] == "python/cpython"
    assert repo["owner"]["login"] == "python"
    assert repo["private"] is False
    print(repo["full_name"], repo["description"])


def main():
    test_repository_data()


if __name__ == "__main__":
    main()
