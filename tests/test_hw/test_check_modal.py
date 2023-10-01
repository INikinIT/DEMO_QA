import pytest
from pages.modal_dialogs import PageDialog
from conftest import browser


def test_dialogs(browser):
    modal_dialogs = PageDialog(browser)

    if not modal_dialogs.code_status():
        pytest.skip(reason=f'Страница {modal_dialogs.base_url} недоступна')

    modal_dialogs.visit()

    assert modal_dialogs.small_modal.exist()
    modal_dialogs.small_modal.click()
    assert modal_dialogs.window.exist()
    assert modal_dialogs.close_small.exist()
    modal_dialogs.close_small.click()
    assert not modal_dialogs.window.exist()

    assert modal_dialogs.large_modal.exist()
    modal_dialogs.large_modal.click()
    assert modal_dialogs.window.exist()
    assert modal_dialogs.close_large.exist()
    modal_dialogs.close_large.click()
    assert not modal_dialogs.window.exist()
