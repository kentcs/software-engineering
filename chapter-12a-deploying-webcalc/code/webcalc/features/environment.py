"""Real Chrome setup for behave; the web app runs in a separate process."""

from pathlib import Path
import re
from urllib.error import URLError
from urllib.request import urlopen

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def before_all(context):
    context.base_url = context.config.userdata.get('base_url', 'http://localhost:8080')
    headless = str(context.config.userdata.get('headless', 'false')).lower()
    if headless not in ('true', 'false'):
        raise ValueError('Use -D headless=true or -D headless=false')
    context.headless = headless == 'true'
    try:
        with urlopen(context.base_url, timeout=5) as response:
            if response.status != 200:
                raise RuntimeError(f'App returned HTTP {response.status}')
    except (URLError, TimeoutError) as error:
        raise RuntimeError(
            f'Cannot reach {context.base_url}. Start the app with python3 main.py '
            'in another terminal, or supply -D base_url=http://host:port'
        ) from error


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    if context.headless:
        options.add_argument('--headless=new')
    options.add_argument('--window-size=1100,900')
    # Selenium Manager locates or obtains the driver for installed Chrome.
    context.browser = webdriver.Chrome(options=options)
    context.add_cleanup(context.browser.quit)
    context.browser.set_page_load_timeout(20)
    context.wait = WebDriverWait(context.browser, 10)


def after_scenario(context, scenario):
    if scenario.status == 'failed' and hasattr(context, 'browser'):
        folder = Path('browser-test-artifacts')
        folder.mkdir(exist_ok=True)
        name = re.sub(r'[^a-zA-Z0-9_-]+', '-', scenario.name).strip('-')
        try:
            context.browser.save_screenshot(str(folder / f'{name}.png'))
        except Exception as error:
            print(f'Could not capture failure screenshot: {error}')
