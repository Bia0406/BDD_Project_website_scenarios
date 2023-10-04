from behave import *


@given('I am on the "Laptops, tablets & software" page')
def step_impl(context):
    context.products_page.navigate_to_first_products_page()


@when('I click on "Laptop laptops"')
def step_impl(context):
    context.products_page.laptop_category()


@when('I click to the sort products and choose to see descending list')
def step_impl(context):
    context.products_page.sort_products()


@then('I choose the most expensive product from the displayed list')
def step_impl(context):
    context.products_page.expensive_products()
