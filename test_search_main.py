import pytest
from selene.support.conditions.be import blank
from selene.support.conditions.have import text
from selene.api import *

url = 'https://google.com'
framework = 'selene'


@pytest.fixture(scope='session', autouse=True)
def init():
    print('init browser configuration')
    browser.open(url)
    browser.driver.maximize_window()


@pytest.fixture(autouse=True)
def quit_browser():
    yield
    browser.quit()


def test_search_selene_is_success():
    browser.element('[name="q"]').should_be(blank).type(framework).press_enter()
    browser.element('[id="search"]').should_have(text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_no_results():
    browser.element('[name="q"]').should_be(blank).type('hsad12412trw').press_enter()
    browser.element(by.css("#topstuff p")).should_have(text('Your search - hsad12412trw - did not match any documents.'))
