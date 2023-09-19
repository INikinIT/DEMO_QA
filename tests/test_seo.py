from pages.demoqa import DemoQa
from conftest import browser


def test_seo(browser):
    demo_qa_pages = DemoQa(browser)

    demo_qa_pages.visit()
    assert browser.title == 'DEMOQA'
