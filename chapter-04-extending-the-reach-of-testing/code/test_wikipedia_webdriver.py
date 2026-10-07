from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def software_suggestion(browser):
    for item in browser.find_elements(By.CSS_SELECTOR, ".cdx-menu-item"):
        if item.is_displayed():
            label = item.text.split("\n", 1)[0]
            if label == "Selenium (software)":
                return item.find_element(By.TAG_NAME, "a")
    return False


def test_wikipedia_search():
    browser = webdriver.Chrome()
    try:
        browser.set_window_size(1280, 900)
        browser.set_page_load_timeout(30)
        browser.get("https://en.wikipedia.org/wiki/Main_Page")
        wait = WebDriverWait(browser, 15)
        search = wait.until(EC.element_to_be_clickable((By.NAME, "search")))
        search.send_keys("Selenium")
        suggestion = wait.until(software_suggestion)
        suggestion.click()
        wait.until(EC.text_to_be_present_in_element(
            (By.ID, "firstHeading"), "Selenium (software)"))
        assert browser.find_element(By.ID, "firstHeading").text == "Selenium (software)"
        heading = wait.until(EC.presence_of_element_located(
            (By.ID, "Selenium_WebDriver")))
        paragraph = heading.find_element(By.XPATH, "following::p[1]")
        text = paragraph.text.strip()
        assert "WebDriver" in text
        print(text)
    finally:
        browser.quit()


def main():
    test_wikipedia_search()


if __name__ == "__main__":
    main()
