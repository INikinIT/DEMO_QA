import time
from pages.demo_alerts import Alerts
from conftest import browser


def test_alert(browser):
    demo_alerts = Alerts(browser)

    demo_alerts.visit()
    assert not demo_alerts.alert()
    demo_alerts.alert_button.click()
    time.sleep(2)
    assert demo_alerts.alert()
    demo_alerts.alert().accept()  # строка закрытие алерта


def test_alert_text(browser):
    demo_alerts = Alerts(browser)

    demo_alerts.visit()
    demo_alerts.alert_button.click()
    time.sleep(2)
    assert demo_alerts.alert().text == 'You clicked a button'
    demo_alerts.alert().accept()
    assert not demo_alerts.alert()


def test_confirm(browser):
    demo_alerts = Alerts(browser)

    demo_alerts.visit()
    demo_alerts.confirm_button.click()
    time.sleep(2)
    demo_alerts.alert().dismiss()
    time.sleep(5)
    assert demo_alerts.confirm.get_text() == "You selected Cancel"


def test_prompt(browser):
    demo_alerts = Alerts(browser)

    demo_alerts.visit()
    demo_alerts.prom_button.click()
    time.sleep(2)
    demo_alerts.alert().send_keys('Name')
    demo_alerts.alert().accept()
    assert demo_alerts.result.get_text() == 'You entered Name'


def test_check_alert(browser):
    demo_alerts = Alerts(browser)

    demo_alerts.visit()
    demo_alerts.time_button.click()
    time.sleep(5)
    assert demo_alerts.alert()
    demo_alerts.alert().accept()
