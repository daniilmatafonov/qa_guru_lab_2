from selene import be, have, by
from conftest import *

framework = 'selene'


def test_search_selene_is_success(init):
    browser.element('[name="q"]').should(be.blank).type(framework).press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_no_results(init):
    browser.element('[name="q"]').should(be.blank).type('hsad12412trw').press_enter()
    browser.element(by.css("#topstuff p")).should(have.text('Your search - hsad12412trw - did not match any documents.'))
