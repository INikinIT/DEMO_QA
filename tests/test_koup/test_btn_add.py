import time

from pages.the_internet import TheInternet
from pages.remove_elements import RemoveElements
from conftest import browser


def test_btn_add(browser):
    btn_add = TheInternet(browser)
    remove_elements = RemoveElements(browser)

    btn_add.visit()
    assert btn_add.add_remove.get_text() == 'Add/Remove Elements'
    btn_add.add_remove.click()
    assert remove_elements.equal_url()

    assert remove_elements.add_element.get_text() == 'Add Element'

    assert remove_elements.add_element.get_dom_attribute('onclick') == 'addElement()'

    for i in range(4):
        remove_elements.add_element.click()
    assert remove_elements.click_add.check_count_elements(4)

    for element in remove_elements.click_add.find_elements():
        assert element.text == 'Delete'
    time.sleep(4)

    while remove_elements.click_add.exist():
        remove_elements.click_add.click()

    assert not remove_elements.click_add.exist()
    time.sleep(4)
