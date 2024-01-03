
from faker import Faker
from behave import *
from page_object.Home_page import HomePage
from page_object.error_or_register import massage
from page_object.register_page import RegisterPage
from selenium.webdriver.support import expected_conditions as EC


@given('I navigate to the register page')
def step_given_navigate_to_register_page(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_myaccount_than_register()


@when('I enter details into mandatory fields')
def step_when_enter_details_mandatory_fields(context):
    faker = Faker()
    context.register_page = RegisterPage(context.driver)
    password = faker.password()
    context.register_page.enter_the_credentials(faker.first_name(), faker.last_name(), faker.email(),
                                                faker.phone_number(), password, password, "select")


@when('I click on the Continue Button')
def step_when_click_continue_button(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.click_submit_button()


@then('the account should be created')
def step_then_account_created(context):
    context.verify_or_massage = massage(context.driver)
    assert context.verify_or_massage.verify_account().__eq__("Your Account Has Been Created! abc")


@when('I enter details into all fields except the email field')
def step_when_enter_details_except_email(context):
    faker = Faker()
    password = faker.password()
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_the_credentials(faker.first_name(), faker.last_name(), "",
                                                faker.phone_number(), password, password, "select")


@when('I enter an existing email into the email field')
def step_when_enter_existing_email(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_email("abc@hotmail.com")


@when('I enter nothing into fields')
def step_when_enter_nothing_into_fields(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_the_credentials("", "", "", "", "", "", "select")


@then('a proper warning message should be displayed')
def step_then_warning_message_displayed(context):
    context.verify_or_massage = massage(context.driver)
    assert context.verify_or_massage.error_massage().__eq__("Warning: E-Mail Address is already registered! abc")


@then('proper warning messages for every field should be displayed')
def step_then_warning_messages_for_every_field_displayed(context):
    context.verify_or_massage = massage(context.driver)
    context.register_page.check_all_assertion()
