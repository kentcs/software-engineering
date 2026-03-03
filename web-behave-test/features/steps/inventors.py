from behave.api.pending_step import StepNotImplementedError

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


@given("we have a browser")
def step_impl(context):
    context.browser = webdriver.Chrome()


@when("go to Wikipedia")
def step_impl(context):
    context.browser.get("http://www.wikipedia.org")
    sleep(1)


@then('"Wikipedia" will be in the page title')
def step_impl(context):
    assert "Wikipedia" in context.browser.title
    sleep(1)


@then("close the browser")
def step_impl(context):
    context.browser.close()


@when('we search for "{invention}"')
def step_impl(context, invention):
    search_box = context.browser.find_element(By.NAME, "search")
    search_box.clear()
    search_box.send_keys(invention)
    search_box.send_keys(Keys.RETURN)
    sleep(2)


@then('"{inventor}" will be in the page content')
def step_impl(context, inventor):
    assert inventor in context.browser.page_source
