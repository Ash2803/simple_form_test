import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def screen_config():
    browser.open('https://google.com').driver.maximize_window()
