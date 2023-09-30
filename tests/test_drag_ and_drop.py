import time
from pages.droppable import Droppable
from conftest import browser
from selenium.webdriver import ActionChains


def test_drag_drop(browser):
    drop_page = Droppable(browser)
    action_chains = ActionChains(browser)

    drop_page.visit()

    assert drop_page.drop.check_css_new("backgroundColor", 'rgba(0, 0, 0, 0)')

    action_chains.drag_and_drop(
        drop_page.drag.find_element(),
        drop_page.drop.find_element()
    ).perform()

    time.sleep(1)

    assert drop_page.drop.check_css_new('backgroundColor', 'rgba(70, 130, 180, 1)')
    time.sleep(5)

    action_chains.drag_and_drop_by_offset(
        drop_page.drag.find_element(),
        -200, 0
    ).perform()

    time.sleep(5)
    assert drop_page.drop.check_css_new('backgroundColor', 'rgba(70, 130, 180, 1)')
