from pages.base_page import BasePage
from components.components import WebElement


class TheInternet(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://the-internet.herokuapp.com/'
        super().__init__(driver, self.base_url)

        self.add_remove = WebElement(driver, '#content > ul > li:nth-child(2) > a')
        # self.add_element = WebElement(driver, 'onclikc="addElement()"')
