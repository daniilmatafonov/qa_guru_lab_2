from selene.support.shared import browser
import pytest


@pytest.fixture(scope='session', autouse=True)
def setup():
    browser.open('https://google.com')
    browser.driver.set_window_size(1360, 768)