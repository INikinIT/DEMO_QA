import time
from pages.web_tables import WebTables
from conftest import browser


def test_check_data(browser):
    web_tables = WebTables(browser)

    web_tables.visit()
    assert web_tables.add_button.exist()
    web_tables.add_button.click()
    web_tables.submit.click()

    web_tables.first_name.send_keys('Joe')
    web_tables.last_name.send_keys('Biden')
    web_tables.email.send_keys('joe@old.yes')
    web_tables.age.send_keys('70')
    web_tables.salary.send_keys('1000')
    web_tables.department.send_keys('Government')

    web_tables.submit.click()

    web_tables.edit.click()
    web_tables.first_name.clear()
    web_tables.first_name.send_keys('Jonny')
    web_tables.submit.click()
    web_tables.delete.click()


def test_tables(browser):
    web_tables = WebTables(browser)

    web_tables.visit()
    assert not web_tables.no_rows.exist()

    while web_tables.delete_3.exist():
        web_tables.delete_3.click()

    time.sleep(2)
    assert web_tables.no_rows.exist()


def test_check_tables(browser):
    web_tables = WebTables(browser)

    web_tables.visit()
    web_tables.rows.click_force()
    web_tables.rows_5.click()
    assert not web_tables.previous.click()
    assert web_tables.previous.get_dom_attribute('disabled')
    assert not web_tables.next.click()
    assert web_tables.next.get_dom_attribute('disabled')

    for i in range(3):
        web_tables.add_button.click()
        web_tables.first_name.send_keys('Joe')
        web_tables.last_name.send_keys('Biden')
        web_tables.email.send_keys('joe@old.yes')
        web_tables.age.send_keys('70')
        web_tables.salary.send_keys('1000')
        web_tables.department.send_keys('Government')
        web_tables.submit.click()

    assert not web_tables.next.get_dom_attribute('disabled')
    web_tables.next.click()
    assert web_tables.str.get_dom_attribute('value') == '2'
    web_tables.previous.click()
    time.sleep(2)
    assert web_tables.str.get_dom_attribute('value') == '1'
    time.sleep(2)
