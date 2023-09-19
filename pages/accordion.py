from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.see_check = WebElement(driver, '#section1Content > p ')
        self.click_check = WebElement(driver, '#section1Heading')
        self.see_section_1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.see_section_2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.see_section_p = WebElement(driver, '#section3Content > p')
