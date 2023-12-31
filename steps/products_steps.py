from behave import *

# Scenariu 1:


@given('I am on the "Laptops, tablets & software" page')
def step_impl(context):
    context.products_page.navigate_to_first_products_page()


@when('I click on "Laptop laptops"')
def step_impl(context):
    context.products_page.laptop_category()


@when('I click to the sort products and choose to see descending list')
def step_impl(context):
    context.products_page.sort_laptop_products()


@then('I choose the most expensive product from the displayed list')
def step_impl(context):
    context.products_page.expensive_product()


# Scenariu 2:


@given('I am on the "Mobile Phones & Gadgets" page')
def step_impl(context):
    context.products_page.navigate_to_second_products_page()


@when('I click on "Mobile Phones"')
def step_impl(context):
    context.products_page.phone_category()


@when('I click to the sort products and choose to see the lowest price from list')
def step_impl(context):
    context.products_page.sort_phone_products()


@then('I choose the cheapest product from the displayed list')
def step_impl(context):
    context.products_page.cheapest_product()


# Scenariu 3:

@given('I am on the "Home & Furniture" page')
def step_impl(context):
    context.products_page.navigate_to_last_product_page()


@when('I click on "Interior and exterior decorations" button')
def step_impl(context):
    context.products_page.decorations_category()


@when('I click on "Christmas tree" button')
def step_impl(context):
    context.products_page.christmas_tree_category()


@when('I click to the sort Christmas tree and choose to see descending list')
def step_impl(context):
    context.products_page.sort_tree_products()


@then('I choose the expensive product from the displayed list')
def step_impl(context):
    context.products_page.expensive_christmas_tree()
