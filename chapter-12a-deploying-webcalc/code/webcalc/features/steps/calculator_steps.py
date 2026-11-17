"""Interact with the rendered app; never import the calculator implementation."""

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

DISPLAY = (By.CSS_SELECTOR, '.font-mono')
SYMBOLS = {'/': '\u00f7', '*': '\u00d7', '-': '\u2212'}


@given('I open the calculator')
def open_calculator(context):
    context.browser.get(context.base_url)
    context.wait.until(EC.visibility_of_element_located(DISPLAY))
    # Wait for NiceGUI's websocket before sending events to its Python handlers.
    context.wait.until(lambda browser: browser.execute_script(
        'return typeof socket !== "undefined" && socket.connected === true;'))
    assert context.browser.find_element(*DISPLAY).text == '0'


@when('I click the buttons "{buttons}"')
def click_buttons(context, buttons):
    for token in buttons.split():
        label = SYMBOLS.get(token, token)
        if label not in ('C', 'CE', '+/-', '\u00f7', '\u00d7', '\u2212', '+', '.', '=',
                         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            raise ValueError(f'Unknown calculator button: {token}')
        locator = (By.XPATH, f'//button[normalize-space(.)="{label}"]')
        context.wait.until(EC.element_to_be_clickable(locator)).click()


@when('I type "{text}"')
def type_text(context, text):
    context.browser.find_element(By.TAG_NAME, 'body').send_keys(text)


@when('I press the "{key}" key')
def press_key(context, key):
    keys = {'Enter': Keys.ENTER, 'Escape': Keys.ESCAPE}
    context.browser.find_element(By.TAG_NAME, 'body').send_keys(keys[key])


@then('the display is "{expected}"')
def check_display(context, expected):
    # Exact equality: a display of 15 must not satisfy an expectation of 5.
    context.wait.until(
        lambda browser: browser.find_element(*DISPLAY).text == expected,
        message=f'Expected calculator display {expected!r}',
    )
    assert context.browser.find_element(*DISPLAY).text == expected
