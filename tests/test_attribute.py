from pages.text_box import TextBox
from conftest import browser


def test_placeholder(browser):
    tests_box = TextBox(browser)

    tests_box.visit()
    assert tests_box.name.get_dom_attribute('placeholder') == 'Full Name'
