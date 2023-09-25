import time
from pages.checkbox import CheckBox
from pages.element_page import ElementsPage
from conftest import browser


def test_find_elements(browser):
    element_page = ElementsPage(browser)
    element_page.visit()
    assert element_page.btn_first_menu.check_count_elements(count=9)


def test_count_checkbox(browser):
    check_page = CheckBox(browser)

    check_page.visit()
    time.sleep(2)
    assert check_page.checkbox.check_count_elements(1)
    check_page.clik_button.click()
    assert check_page.checkbox.check_count_elements(17)
    browser.refresh()
    assert check_page.checkbox.check_count_elements(1)
