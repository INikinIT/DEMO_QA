import time

import pytest
from pages.demoqa import DemoQa
from pages.radio_button import RadioButton
from conftest import browser


@pytest.mark.skip
def test_decor_3(browser):
    demo_qa = DemoQa(browser)

    demo_qa.visit()
    assert demo_qa.check_decor.check_count_elements(6)

    for element in demo_qa.check_decor.find_elements():
        assert not element.text == ''


# @pytest.mark.skipif(True, reason='просто пропуск')
def test_radio_button(browser):
    radio_button = RadioButton(browser)

    if not radio_button.code_status():
        pytest.skip(reason=f'Страница {radio_button.base_url} недоступна')

    radio_button.visit()
    radio_button.yes.click_force()
    assert radio_button.text_check.get_text() == 'You have selected Yes'

    radio_button.impressive.click_force()
    assert radio_button.text_check.get_text() == 'You have selected Impressive'
    assert radio_button.no.get_dom_attribute('class')
