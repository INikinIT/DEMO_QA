import time
from pages.progress_bar import ProgressBar
from conftest import browser


def test_progress_bar(browser):
    progress_bar = ProgressBar(browser)

    progress_bar.visit()
    time.sleep(2)
    progress_bar.start_stop.click()
    if progress_bar.progress.get_dom_attribute('aria-valuenow') == '51':
        progress_bar.start_stop.click()
