from pages.modal_dialogs import PageDialog
from conftest import browser


def test_modal_elements(browser):
    modal_elements = PageDialog(browser)

    modal_elements.visit()
    assert modal_elements.check_quantity.check_count_elements(5)
