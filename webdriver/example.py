from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
browser.get("https://www.selenium.dev/selenium/web/web-form.html")
title = browser.title
print(title)
assert title > ""
text_box = browser.find_element(by=By.NAME, value="my-text")
text_box.send_keys("hello there")

browser.implicitly_wait(0.5)

sleep(5)
