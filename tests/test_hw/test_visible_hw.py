import time
from pages.accordion import Accordion
from conftest import browser


def test_visible_accordion(browser):
    visible_accordion = Accordion(browser)

    visible_accordion.visit()
    assert visible_accordion.see_check.visible()
    visible_accordion.click_check.click()
    time.sleep(2)
    assert not visible_accordion.see_check.visible()


def test_visible_accordion_default(browser):
    visible_accordion = Accordion(browser)

    visible_accordion.visit()
    assert not visible_accordion.see_section_1.visible()
    assert not visible_accordion.see_section_2.visible()
    assert not visible_accordion.see_section_p.visible()
