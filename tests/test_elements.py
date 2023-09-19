from pages.element_page import ElementsPage
from conftest import browser


def test_find_elements(browser):
    element_page = ElementsPage(browser)
    element_page.visit()
    assert element_page.btn_first_menu.check_count_elements(9)
