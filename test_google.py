import pytest
from selene import be, have
from selene.support.shared import browser


def test_selene_search():
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_negative_search_():
    browser.element('[name="q"]').should(be.blank).type('fdsf436sdf').press_enter()
    browser.element('p[aria-level]').should(have.text('По запросу fdsf436sdf ничего не найдено'))
