import time
from pages.demoqa import DemoQa
from pages.element_page import ElementsPage
from conftest import browser


def test_size(browser):
    demo_qa_pages = DemoQa(browser)
    demo_qa_pages.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)


def test_visible_nav_bar(browser):
    element_page = ElementsPage(browser)

    element_page.visit()
    assert not element_page.check_mobile.visible()
    browser.set_window_size(360, 740)
    assert element_page.check_mobile.visible()
    browser.set_window_size(1000, 1000)
