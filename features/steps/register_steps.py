import time
from behave import *
# from assertpy import soft_assertions, assert_that
from page_objects.home_page import HomePage
from utilities.generate_testdata import TestdataGenerator



@given(u'User click on My Account > Register menu')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account_menu()
    context.register_page = context.home_page.click_on_register_link()

@when(u'User enter below details into mandatory fields')
def step_impl(context):
    for row in context.table:
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        context.register_page.enter_email(row["email"])
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.enter_password(row["password"])
        context.register_page.confirm_password(row["password"])


@when(u'User select Privacy Policy option')
def step_impl(context):
    context.register_page.accept_privacy_policy_check()
    time.sleep(1)


@when(u'User click on Continue button')
def step_impl(context):
    context.account_page = context.register_page.click_on_continue_button()
    time.sleep(1)


@then(u'User account should get created successfully')
def step_impl(context):
    assert context.account_page.display_status_of_new_account_created_heading()
    time.sleep(1)


@when(u'User enter details into all fields')
def step_impl(context):
    context.register_page.enter_first_name(TestdataGenerator.get_first_name())
    context.register_page.enter_last_name(TestdataGenerator.get_last_name())
    context.register_page.enter_email(TestdataGenerator.get_email())
    context.register_page.enter_telephone(TestdataGenerator.get_telephone())
    password = TestdataGenerator.get_password()
    context.register_page.enter_password(password)
    context.register_page.confirm_password(password)
    context.register_page.subscribe_newsletter()


@when(u'User enter details into all fields except email field')
def step_impl(context):
    context.register_page.enter_first_name(TestdataGenerator.get_first_name())
    context.register_page.enter_last_name(TestdataGenerator.get_last_name())
    context.register_page.enter_telephone(TestdataGenerator.get_telephone())
    password = TestdataGenerator.get_password()
    context.register_page.enter_password(password)
    context.register_page.confirm_password(password)
    context.register_page.subscribe_newsletter()


@when(u'User enter existing accounts email into email field')
def step_impl(context):
    context.register_page.enter_email("demoqa03@testmail.com")


@then(u'Proper warning message about duplicate account should be displayed')
def step_impl(context):
    assert context.register_page.check_email_already_registered_warning()
    time.sleep(1)


@when(u'User dont enter anything into the fields')
def step_impl(context):
    context.register_page.enter_first_name("")
    context.register_page.enter_last_name("")
    context.register_page.enter_email("")
    context.register_page.enter_telephone("")
    context.register_page.enter_password("")
    context.register_page.confirm_password("")


@then(u'Proper warning messages for missing mandatory fields should be displayed')
# @soft_assertions
def step_impl(context):
    assert context.register_page.check_all_field_warnings()
    time.sleep(1)