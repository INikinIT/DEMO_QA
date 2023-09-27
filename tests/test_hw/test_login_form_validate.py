from pages.form_page import FormPage
from conftest import browser


def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert form_page.check_first_name.get_dom_attribute('placeholder') == 'First Name'
    assert form_page.check_last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert form_page.check_user_email.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
    form_page.btn_submit.click_force()
    assert form_page.user_form.get_dom_attribute('class') == 'was-validated'  #
