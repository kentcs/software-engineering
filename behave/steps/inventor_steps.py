from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


@given(u'we have navigated to wikipedia')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("http://www.wikipedia.org")
    sleep(1)


@when(u'we search for "{invention}"')
def step_impl(context, invention):
    search_element = context.browser.find_element(By.ID, "searchInput")
    search_element.clear()
    search_element.send_keys(invention)
    search_element.send_keys(Keys.RETURN)
    sleep(1)


@then(u'the resulting page will include "{inventor}"')
def step_impl(context, inventor):
    assert inventor in context.browser.page_source
