from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# def test_light_bulb_inventor():
#     print("testing light_bulb_inventor")
#     browser = webdriver.Chrome()
#     browser.get("https://www.wikipedia.org")
#     assert "Wikipedia" in browser.title
#     sleep(2)
#     search_box = browser.find_element(by=By.ID, value="searchInput")
#     search_box.send_keys("light bulb")    
#     # search_button = context.browser.find_element(by=By.CSS_SELECTOR, value="button")
#     # search_button.click()
#     search_box.send_keys(Keys.RETURN)
#     sleep(2)
#     # assert that we are on the light bulb page
#     text = browser.find_element(by=By.XPATH, value="/html/body").text
#     assert "light bulb" in text
#     # assert that Thomas Edison is also on that page
#     assert "Thomas Edison" in text

# def test_airplane_inventor():
#     print("testing airplane_inventor")
#     browser = webdriver.Chrome()
#     browser.get("https://www.wikipedia.org")
#     assert "Wikipedia" in browser.title
#     sleep(2)
#     search_box = browser.find_element(by=By.ID, value="searchInput")
#     search_box.send_keys("airplane")    
#     # search_button = context.browser.find_element(by=By.CSS_SELECTOR, value="button")
#     # search_button.click()
#     search_box.send_keys(Keys.RETURN)
#     sleep(2)
#     # assert that we are on the light bulb page
#     text = browser.find_element(by=By.XPATH, value="/html/body").text
#     assert "airplane" in text
#     # assert that Thomas Edison is also on that page
#     assert "Wright" in text

#     helicopter
#     Sikorsky

def test_inventor(invention, inventor):
    print("testing invention")
    browser = webdriver.Chrome()
    browser.get("https://www.wikipedia.org")
    assert "Wikipedia" in browser.title
    sleep(2)
    search_box = browser.find_element(by=By.ID, value="searchInput")
    search_box.send_keys(invention)    
    # search_button = context.browser.find_element(by=By.CSS_SELECTOR, value="button")
    # search_button.click()
    search_box.send_keys(Keys.RETURN)
    sleep(2)
    # assert that we are on the invention page
    text = browser.find_element(by=By.XPATH, value="/html/body").text
    assert invention in text
    # assert that the inventor is also on that page
    assert inventor in text


if __name__ == "__main__":
    # test_light_bulb_inventor()
    # test_airplane_inventor()
    # test_inventor("light bulb","Edison")
    # test_inventor("airplane","Wright")
    # test_inventor("helicopter","Sikorsky")

    for item in [
        ("light bulb","Edison"),
        ("airplane","Wright"),
        ("helicopter","Sikorsky")
    ]:
        invention, inventor = item
        test_inventor(invention, inventor)

# browser.implicitly_wait(0.5)

