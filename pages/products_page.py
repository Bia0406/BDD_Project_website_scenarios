from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


from base_page import BasePage


class ProductsPage(BasePage):
    FIRST_BTN_PRODUCTS = f"{BasePage._BASE_URL}/laptopuri,-tablete-~-software/"
    LAPTOP_BTN = (By.XPATH, '//div[text()="Laptop laptopuri"]')
    SORT_BTN = (By.ID, "sortare")
    EXPENSIVE_PRODUCTS = (By.XPATH, "//span[text()='39276']")

    def navigate_to_first_products_page(self):
        self.browser.get(self.FIRST_BTN_PRODUCTS)

    def laptop_category(self):
        self.click(locator=self.LAPTOP_BTN)

    def sort_products(self):
        self.click(locator=self.SORT_BTN)
        select_obj = Select(self.browser.find_element(*self.SORT_BTN))
        select_obj.select_by_visible_text('Pret descrescator')

    def expensive_products(self):
        assert self.is_displayed(locator=self.EXPENSIVE_PRODUCTS)

