from pages.base_page import BasePage
from components.components import WebElement


class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.add_button = WebElement(driver, '#addNewRecordButton')
        self.check_none = WebElement(driver, '#userForm > div > div > [type=text]')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.submit = WebElement(driver, '#submit')
        self.edit = WebElement(driver, '#edit-record-4 > svg > path')
        self.delete = WebElement(driver, '#delete-record-4 > svg > path')
