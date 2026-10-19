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
    # Set up the precondition: a named place, or any URL, opened in Chrome.
    url = LOCATIONS.get(location, location)
    context.browser = webdriver.Chrome()
    context.add_cleanup(context.browser.quit)
    context.wait = WebDriverWait(context.browser, 15)
    context.browser.get(url)
    # Verify it: the browser loaded a real page.
    assert context.browser.title, "the page has no title"


@when("I search for {invention}")
def search_for_invention(context, invention):
    start = context.browser.current_url
    box = context.browser.find_element(By.NAME, "search")
    box.send_keys(invention, Keys.ENTER)
    # Verify the action was taken: we left the home page for an article.
    context.wait.until(EC.url_changes(start))
    heading = context.browser.find_element(By.ID, "firstHeading").text
    assert not heading.startswith("Search results"), heading


@then("the page text contains {inventor}")
def page_text_contains_inventor(context, inventor):
    text = context.browser.find_element(By.TAG_NAME, "body").text
    assert inventor in text
