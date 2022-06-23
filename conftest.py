from selene.support.shared import browser
import pytest

url = 'https://google.com'


@pytest.fixture(scope='session', autouse=True)
def config():
    browser.config.window_width = 1360
    browser.config.window_height = 768


@pytest.fixture
def init():
    browser.open(url)
