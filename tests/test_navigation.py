from pages.demoqa import DemoQa
from pages.element_page import ElementsPage
from conftest import browser


def test_navigation(browser):
    demo_qa_page = DemoQa(browser)
    element_page = ElementsPage(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    element_page.driver.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    element_page.equal_url()
