from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


from base_page import BasePage


class ProductsPage(BasePage):
    FIRST_BTN_PRODUCTS = f"{BasePage._BASE_URL}/laptopuri,-tablete-~-software/"
    SECOND_BTN_PRODUCTS = f"{BasePage._BASE_URL}/telefoane-mobile-~-gadget/"
    LAPTOP_BTN = (By.XPATH, '//div[text()="Laptop laptopuri"]')
    PHONE_BTN = (By.XPATH, "//div[text()='Telefoane Mobile']")
    SORT_BTN = (By.ID, "sortare")
    EXPENSIVE_LAPTOP = (By.XPATH, "//span[text()='39276']")
    CHEAPEST_PHONE = (By.XPATH, '//span[text()="59"]')

    def navigate_to_first_products_page(self):
        self.browser.get(self.FIRST_BTN_PRODUCTS)

    def navigate_to_second_products_page(self):
        self.browser.get(self.SECOND_BTN_PRODUCTS)

    def laptop_category(self):
        self.click(locator=self.LAPTOP_BTN)

    def phone_category(self):
        self.click(locator=self.PHONE_BTN)

    def sort_laptop_products(self):
        self.click(locator=self.SORT_BTN)
        select_obj = Select(self.browser.find_element(*self.SORT_BTN))
        select_obj.select_by_visible_text('Pret descrescator')

    def sort_phone_products(self):
        self.click(locator=self.SORT_BTN)
        select_obj = Select(self.browser.find_element(*self.SORT_BTN))
        select_obj.select_by_index(2)

    def expensive_product(self):
        assert self.is_displayed(locator=self.EXPENSIVE_LAPTOP)

    def cheapest_product(self):
        assert self.is_displayed(locator=self.CHEAPEST_PHONE)

