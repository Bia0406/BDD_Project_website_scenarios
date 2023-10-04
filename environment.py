from browser import Browser
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def before_all(context):
    """
    Vom defini toate instructiuniile care trebuie executate
    inainte rularii tuturor pasiilor
    """
    context.browser = Browser()
    context.login_page = LoginPage()
    context.products_page = ProductsPage()

def after_all(context):
    """
    Vom defini toate instructiuniile care trebuie executate
    dupa rularea tuturor pasiilor
    """
    context.browser.close()
