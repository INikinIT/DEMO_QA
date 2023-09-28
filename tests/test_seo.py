import time
import pytest
from pages.accordion import Accordion
from pages.demo_alerts import Alerts
from pages.browser_tab import BrowserTab
from pages.demoqa import DemoQa
from conftest import browser


def test_seo(browser):
    demo_qa_pages = DemoQa(browser)

    demo_qa_pages.visit()
    assert browser.title == 'DEMOQA'


@pytest.mark.parametrize('pages', [Accordion, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'
