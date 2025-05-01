import time
from behave import *
from page_objects.home_page import HomePage
from utilities.read_config import read_configuration


@given(u'User navigated to app home page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    assert context.home_page.check_home_page_title(read_configuration('search page info', 'page_title'))
    time.sleep(1)


@when(u'User enters valid product say "{product}" into the search box field')
def step_impl(context, product):
    context.home_page.enter_product_into_search_box_field(product)


@when(u'click on search button')
def step_impl(context):
    context.search_page = context.home_page.click_on_search_button()
    time.sleep(1)


@then(u'Valid product should get displayed in Search results')
def step_impl(context):
    assert context.search_page.display_status_of_searched_product()


@when(u'User enters invalid product say "{product}" into the search box field')
def step_impl(context, product):
    context.home_page.enter_product_into_search_box_field(product)


@then(u'Proper message should be displayed in Search results')
def step_impl(context):
    assert context.search_page.display_status_of_warning_message(
        read_configuration('search page info', 'invalid_product_search_warning'))


@when(u'User dont enter anything into search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box_field("")
