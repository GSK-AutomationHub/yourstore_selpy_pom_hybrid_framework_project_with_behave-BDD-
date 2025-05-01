import time
from behave import *
from page_objects.home_page import HomePage


@given(u'User click on My Account > Login menu')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account_menu()
    context.login_page = context.home_page.click_on_login_link()


@when(u'User enters valid email address say "{email}" as username')
def step_impl(context,email):
    context.login_page.enter_email_address(email)


@when(u'User enters valid password say "{password}" as password')
def step_impl(context,password):
    context.login_page.enter_password(password)


@when(u'click on login button')
def step_impl(context):
    context.account_page = context.login_page.click_on_login_button()
    time.sleep(1)


@then(u'User should get logged in successfully')
def step_impl(context):
    assert context.account_page.display_status_of_edit_account_info_link()


@when(u'User enters invalid email address "{email}" as username')
def step_impl(context,email):
    context.login_page.enter_email_address(email)


@when(u'User enters invalid password "{password}" as password')
def step_impl(context,password):
    context.login_page.enter_password(password)


@then(u'Proper warning message should be displayed')
def step_impl(context):
    assert context.login_page.display_status_of_invalid_login_warning_message()




