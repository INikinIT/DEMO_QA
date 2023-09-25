from pages.text_box import TextBox
from conftest import browser


def test_text_box(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.name.send_keys('My name')
    text_box.address.send_keys('Spb.ru')
    text_box.btn_submit.click()
    assert text_box.check_name.get_text() == 'Name:My name'
    assert text_box.check_address.get_text() == 'Current Address :Spb.ru'
