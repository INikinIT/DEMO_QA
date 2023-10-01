from pages.web_tables import WebTables
from conftest import browser


def test_sort(browser):
    web_tables = WebTables(browser)

    web_tables.visit()

    for element in web_tables.head_page.find_elements():
        element.click()
        assert element.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
