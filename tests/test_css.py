from pages.element_page import ElementsPage
from conftest import browser


def test_flex_menu(browser):
    element_page = ElementsPage(browser)

    element_page.visit()
    assert element_page.block_menu.check_css('flex', '0 0 25%')
    assert element_page.block_menu.check_css('max-width', '25%')
    browser.set_window_size(360, 740)
    assert element_page.block_menu.check_css('flex', '0 0 100%')
    assert element_page.block_menu.check_css('max-width', '100%')
    browser.set_window_size(1000, 1000)