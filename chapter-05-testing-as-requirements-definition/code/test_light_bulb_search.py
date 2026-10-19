from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_light_bulb_mentions_edison():
    browser = webdriver.Chrome()
    try:
        browser.get("https://en.wikipedia.org/wiki/Main_Page")
        wait = WebDriverWait(browser, 15)
        search = wait.until(EC.element_to_be_clickable((By.NAME, "search")))
        start = browser.current_url
        search.send_keys("light bulb", Keys.ENTER)
        wait.until(EC.url_changes(start))
        wait.until(EC.visibility_of_element_located((By.ID, "firstHeading")))
        text = browser.find_element(By.TAG_NAME, "body").text
        assert "Edison" in text
    finally:
        browser.quit()


def main():
    test_light_bulb_mentions_edison()


if __name__ == "__main__":
    main()
