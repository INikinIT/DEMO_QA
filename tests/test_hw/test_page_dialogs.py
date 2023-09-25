from pages.modal_dialogs import PageDialog
from pages.demoqa import DemoQa
from conftest import browser


def test_modal_elements(browser):
    modal_elements = PageDialog(browser)

    modal_elements.visit()
    assert modal_elements.check_quantity.check_count_elements(5)


def test_navigation_modal(browser):
    modal_elements = PageDialog(browser)
    demo_qa = DemoQa(browser)

    modal_elements.visit()
    browser.refresh()
    modal_elements.tools_qa.click_force()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert demo_qa.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)  #
