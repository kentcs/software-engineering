from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


def test_we_can_get_to_wikipedia():
    print("test we can get to wikipedia")
    browser = webdriver.Chrome()
    browser.get("http://www.wikipedia.org")
    assert "Wikipedia" in browser.title
    browser.close()


def test_does_edison_get_credit():
    print("test does edison get credit")
    browser = webdriver.Chrome()
    browser.get("http://www.wikipedia.org")
    assert "Wikipedia" in browser.title
    search_box = browser.find_element(By.NAME, "search")
    search_box.clear()
    search_box.send_keys("light bulb")
    search_box.send_keys(Keys.RETURN)
    sleep(2)
    assert "Thomas Edison" in browser.page_source
    browser.close()


def test_does_sikorsky_get_credit():
    print("test does sikorsky get credit")
    browser = webdriver.Chrome()
    browser.get("http://www.wikipedia.org")
    assert "Wikipedia" in browser.title
    search_box = browser.find_element(By.NAME, "search")
    search_box.clear()
    search_box.send_keys("helicopter")
    search_box.send_keys(Keys.RETURN)
    sleep(2)
    assert "Sikorsky" in browser.page_source
    browser.close()


if __name__ == "__main__":
    test_we_can_get_to_wikipedia()
    test_does_edison_get_credit()
    test_does_sikorsky_get_credit()
    print("done.")
