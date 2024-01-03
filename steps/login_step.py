from behave import *
from faker import Faker

from page_object.Home_page import HomePage
from page_object.login_page import LoginPage
from page_object.verify_login_page import VerifyLogin


@given(u'I naviagte to Login Page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_myaccount_than_login()


@when(u'I enter valid email as "{email}" and valid password as "{password}" into fields')
def step_impl(context, email, password):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email(email)
    context.login_page.enter_password(password)


@when(u'I click on Login Button')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.click_submit_button()


@then(u'I login into the page')
def step_impl(context):
    context.verify_page = VerifyLogin(context.driver)
    assert context.verify_page.verify_login()


@when(u'I enter invalid email and valid password into fields')
def step_impl(context):
    faker = Faker()
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email(faker.email())
    context.login_page.enter_password("123456789")


@then(u'I should get proper warning massage')
def step_impl(context):
    context.verify_page = VerifyLogin(context.driver)
    assert context.verify_page.error_massage_verify().__eq__("Warning: No match for E-Mail ""Address and/or Password.")


@when(u'I enter valid email and invalid password into fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email("abc@hotmail.com")
    context.login_page.enter_password("1234567890")


@when(u'I enter invalid email and invalid password into fields')
def step_impl(context):
    faker = Faker()
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email(faker.email())
    context.login_page.enter_password(faker.password())


@when(u'I leave empty email password fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email("")
    context.login_page.enter_password("")
