import time
from pages.slider import Slider
from conftest import browser
from selenium.webdriver import ActionChains


def test_check_slider(browser):
    slider_page = Slider(browser)
    action_chains = ActionChains(browser)

    slider_page.visit()
    time.sleep(3)
    assert slider_page.check_slider.exist()
    assert slider_page.text_slider.exist()
    assert slider_page.check_slider.get_dom_attribute('value') == '25'

    action_chains.drag_and_drop_by_offset(
        slider_page.check_slider.find_element(),
        0, 0
    ).perform()
    assert slider_page.text_slider.get_dom_attribute('value') == '50'
