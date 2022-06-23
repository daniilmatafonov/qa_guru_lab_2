from selene.support.shared import browser
import pytest


@pytest.fixture(scope='session', autouse=True)
def setup():
    browser.config.window_width = 1360
    browser.config.window_height = 768


@pytest.fixture
def init_browser():
    browser.open('https://google.com')