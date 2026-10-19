from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOCATIONS = {
    "the Wikipedia home page": "https://en.wikipedia.org/wiki/Main_Page",
}


@given("I have opened {location}")
def open_location(context, location):
    url = LOCATIONS.get(location, location)
    context.browser = webdriver.Chrome()
    context.add_cleanup(context.browser.quit)
    context.wait = WebDriverWait(context.browser, 15)
    context.browser.get(url)
    assert context.browser.title, "the page has no title"


@when("I search for {subject}")
def search_for(context, subject):
    start = context.browser.current_url
    box = context.browser.find_element(By.NAME, "search")
    box.send_keys(subject, Keys.ENTER)
    context.wait.until(EC.url_changes(start))
    heading = context.browser.find_element(By.ID, "firstHeading").text
    assert not heading.startswith("Search results"), heading


@then("the page text contains {text}")
def page_text_contains(context, text):
    page = context.browser.find_element(By.TAG_NAME, "body").text
    assert text in page
