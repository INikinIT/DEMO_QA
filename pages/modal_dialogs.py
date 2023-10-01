from pages.base_page import BasePage
from components.components import WebElement


class PageDialog(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.check_quantity = WebElement(driver, '.element-list.collapse.show >  ul > li.btn.btn-light')
        self.tools_qa = WebElement(driver, 'header > a > img')
        self.small_modal = WebElement(driver, '#showSmallModal')
        self.large_modal = WebElement(driver, '#showLargeModal')
        self.window = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.close_small = WebElement(driver, '#closeSmallModal')
        self.close_large = WebElement(driver, '#closeLargeModal')
