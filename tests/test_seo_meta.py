import time
import pytest
from pages.accordion import Accordion
from pages.demo_alerts import Alerts
from pages.browser_tab import BrowserTab
from pages.demoqa import DemoQa
from conftest import browser


@pytest.mark.parametrize('pages', [Accordion, Alerts, DemoQa, BrowserTab])
def test_seo_meta(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(2)
    assert page.metaView.exist()
    assert page.metaView.get_dom_attribute('name') == "viewport"
    assert page.metaView.get_dom_attribute('content') == "width=device-width,initial-scale=1"
