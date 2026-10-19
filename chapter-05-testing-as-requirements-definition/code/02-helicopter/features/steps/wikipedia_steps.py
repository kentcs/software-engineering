from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("I have opened the Wikipedia home page")
def open_home_page(context):
    # Set up the precondition...
    context.browser = webdriver.Chrome()
    context.add_cleanup(context.browser.quit)
    context.wait = WebDriverWait(context.browser, 15)
    context.browser.get("https://en.wikipedia.org/wiki/Main_Page")
    # ...and verify it: the home page is up and its search box is usable.
    context.wait.until(EC.element_to_be_clickable((By.NAME, "search")))


@when("I search for Light Bulb")
def search_for_light_bulb(context):
    start = context.browser.current_url
    box = context.browser.find_element(By.NAME, "search")
    box.send_keys("Light Bulb", Keys.ENTER)
    # Verify the action was taken: we left the home page for an article.
    context.wait.until(EC.url_changes(start))
    heading = context.browser.find_element(By.ID, "firstHeading").text
    assert not heading.startswith("Search results"), heading


@then("the page text contains Edison")
def page_text_contains_edison(context):
    text = context.browser.find_element(By.TAG_NAME, "body").text
    assert "Edison" in text


@when("I search for Helicopter")
def search_for_helicopter(context):
    start = context.browser.current_url
    box = context.browser.find_element(By.NAME, "search")
    box.send_keys("Helicopter", Keys.ENTER)
    # Verify the action was taken: we left the home page for an article.
    context.wait.until(EC.url_changes(start))
    heading = context.browser.find_element(By.ID, "firstHeading").text
    assert not heading.startswith("Search results"), heading


@then("the page text contains Sikorsky")
def page_text_contains_sikorsky(context):
    text = context.browser.find_element(By.TAG_NAME, "body").text
    assert "Sikorsky" in text
