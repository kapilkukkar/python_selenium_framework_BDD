from behave import *
from page_object.Home_page import HomePage
from page_object.search_page import SearchPage


@given(u'i got navigated to Home Page')
def step_impl(context):
    pass


@when(u'i entered valid product into the search box')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.search_box_element("HP")


@when(u'i click on search button')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.search_button()


@then(u'valid product should be shown in search result')
def step_impl(context):
    context.search_page = SearchPage(context.driver)
    assert context.search_page.check_for_item()


@when(u'i entered the invalid product in search box')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.search_box_element("honda")


@then(u'proper error massage should be displayed')
def step_impl(context):
    context.search_page = SearchPage(context.driver)
    assert context.search_page.verify_massage().__contains__("There is no product that matches the search criteria.")


@when(u'i entered the nothing product in search box')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.search_box_element("")
