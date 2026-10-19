import os
import re

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def before_all(context):
    # Once per run: start one browser for every scenario to share.
    context.browser = webdriver.Chrome()
    context.wait = WebDriverWait(context.browser, 15)


def before_scenario(context, scenario):
    # Once per scenario: reset what a scenario could leave behind.
    context.browser.delete_all_cookies()


def after_scenario(context, scenario):
    # Teardown can look at the outcome. Keep a picture of failures.
    if scenario.status == "failed":
        name = re.sub(r"\W+", "-", scenario.name).strip("-").lower()
        os.makedirs("screenshots", exist_ok=True)
        context.browser.save_screenshot(f"screenshots/{name}.png")


def after_all(context):
    context.browser.quit()
