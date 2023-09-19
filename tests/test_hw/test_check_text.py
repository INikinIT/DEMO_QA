from pages.demoqa import DemoQa
from pages.element_page import ElementsPage
from conftest import browser


def test_text_compare(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.text_equals.get_text()


def test_check_text(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    demo_qa_page.text_element.click()
    elements_page.equal_url()
    assert elements_page.text_pleas.get_text()
