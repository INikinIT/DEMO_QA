from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class WebElement:
    def __init__(self, driver, locator=''):
        self.locator = locator
        self.driver = driver
        self.sample = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED'
        self.sample_2 = 'Please select an item from left to start practice'

    def click(self):
        self.find_element().click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        return str(self.find_element().text)

    def check_text(self):

        try:
            self.find_element().text == self.sample
        except NoSuchElementException:
            return False
        return True
