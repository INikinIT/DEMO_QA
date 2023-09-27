from pages.web_tables import WebTables
from conftest import browser


def test_check_data(browser):
    web_tables = WebTables(browser)

    web_tables.visit()
    assert web_tables.add_button.exist()
    web_tables.add_button.click()
    for i in range(6):
        assert web_tables.check_none.get_text() != ''

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
