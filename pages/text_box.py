from pages.base_page import BasePage
from components.components import WebElement


class TextBox(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.name = WebElement(driver, '#userName')
        self.address = WebElement(driver, '#currentAddress.form-control')
        self.btn_submit = WebElement(driver, '#submit')
        self.check_name = WebElement(driver, '#name')
        self.check_address = WebElement(driver, 'p#currentAddress')
