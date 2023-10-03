from behave import *


@given("I am on the login page")
def step_impl(context):
    context.login_page.navigate_to_login_page()


@when('I insert "{email}" email')
def step_impl(context, email):
    context.login_page.insert_email(email)


@when('I insert a password')
def step_impl(context):
    context.login_page.insert_password()


@when("I click the connect button")
def step_impl(context):
    context.login_page.click_login_button()


@when("I click the cookies button")
def step_impl(context):
    context.login_page.click_cookies_button()


@then("Error is displayed")
def step_impl(context):
    context.login_page.error_msg_is_displayed()



