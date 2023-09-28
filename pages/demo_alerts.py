
from pages.base_page import BasePage
from components.components import WebElement


class Alerts(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        self.alert_button = WebElement(driver, '#alertButton')
        self.confirm_button = WebElement(driver, '#confirmButton')
        self.prom_button = WebElement(driver, '#promtButton')
        self.confirm = WebElement(driver, '#confirmResult')
        self.result = WebElement(driver, '#promptResult')
        self.time_button = WebElement(driver, '#timerAlertButton')
