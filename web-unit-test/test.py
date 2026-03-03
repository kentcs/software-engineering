from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
sleep(5)
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
sleep(5)
assert "No results found." not in driver.page_source
driver.close()
print("done.")
