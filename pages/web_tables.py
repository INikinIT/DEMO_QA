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
        self.no_rows = WebElement(driver, 'div.rt-noData')
        self.delete_3 = WebElement(driver, 'span[title="Delete"]')

        self.rows = WebElement(driver, '.-pageSizeOptions > select')
        self.rows_5 = WebElement(driver, 'option:nth-child(1)')
        self.previous = WebElement(driver, ' .-previous > button')
        self.next = WebElement(driver, '.-next > button')
        self.str = WebElement(driver, 'input[type=number]')

        self.head_first = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(1)')
        self.head_name = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(2)')
        self.head_age = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(3)')
        self.head_email = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(4)')
        self.head_salary = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(5)')
        self.head_department = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(6)')
        self.head_action = WebElement(driver, 'div.rt-thead.-header > div > div:nth-child(7)')
        self.head_page = WebElement(driver, 'div.rt-thead.-header > div > div')
