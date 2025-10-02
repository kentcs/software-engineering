from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

@given(u'we navigate to Wikipedia')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://www.wikipedia.org")
    assert "Wikipedia" in context.browser.title
    sleep(2)


@when(u'we search for "{invention}"')
def step_impl(context, invention):
    browser = context.browser
    search_box = browser.find_element(by=By.ID, value="searchInput")
    search_box.send_keys(invention)    
    search_box.send_keys(Keys.RETURN)
    sleep(2)
    text = browser.find_element(by=By.XPATH, value="/html/body").text
    assert invention in text



@then(u'we see that {inventor} is mentioned')
def step_impl(context, inventor):
    browser = context.browser
    text = browser.find_element(by=By.XPATH, value="/html/body").text
    assert inventor in text
