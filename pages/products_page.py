from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


from base_page import BasePage


class ProductsPage(BasePage):
    FIRST_BTN_PRODUCTS = f"{BasePage._BASE_URL}/laptopuri,-tablete-~-software/"
    SECOND_BTN_PRODUCTS = f"{BasePage._BASE_URL}/telefoane-mobile-~-gadget/"
    LAST_BTN_PRODUCTS = f"{BasePage._BASE_URL}/casa-~-mobilier/"
    LAPTOP_BTN = (By.XPATH, '//div[text()="Laptop laptopuri"]')
    PHONE_BTN = (By.XPATH, "//div[text()='Telefoane Mobile']")
    DECORATIONS_BTN = (By.XPATH, '//div[text()="Decoratiuni Interioare si Exterioare"]')
    CRS_TREE_BTN = (By.XPATH, '//div[text()="Brazi de Craciun"]')
    SORT_BTN = (By.ID, "sortare")
    EXPENSIVE_LAPTOP = (By.XPATH, "//span[text()='Laptop Lenovo ThinkPad P1 Gen5 Intel Core i9-12900H 16inch RAM 16GB SSD 512GB nVidia RTX A5500 16GB Win 11 Pro Black 21DC0014RI']")
    CHEAPEST_PHONE = (By.XPATH, '//span[text()="59"]')
    EXPENSIVE_CHRISTMAS_TREE = (By.XPATH, "//span[text()='Brad artificial verde nins 4079 ramuri Aspen 3.00 m']")

    def navigate_to_first_products_page(self):
        self.browser.get(self.FIRST_BTN_PRODUCTS)

    def navigate_to_second_products_page(self):
        self.browser.get(self.SECOND_BTN_PRODUCTS)

    def navigate_to_last_product_page(self):
        self.browser.get(self.LAST_BTN_PRODUCTS)

    def laptop_category(self):
        self.click(locator=self.LAPTOP_BTN)

    def phone_category(self):
        self.click(locator=self.PHONE_BTN)

    def decorations_category(self):
        self.click(locator=self.DECORATIONS_BTN)

    def christmas_tree_category(self):
        self.click(locator=self.CRS_TREE_BTN)

    def sort_laptop_products(self):
        self.click(locator=self.SORT_BTN)
        select_obj = Select(self.browser.find_element(*self.SORT_BTN))
        select_obj.select_by_visible_text('Pret descrescator')

    def sort_phone_products(self):
        self.click(locator=self.SORT_BTN)
        select_obj = Select(self.browser.find_element(*self.SORT_BTN))
        select_obj.select_by_index(2)

    def sort_tree_products(self):
        self.click(locator=self.SORT_BTN)
        select_obj = Select(self.browser.find_element(*self.SORT_BTN))
        select_obj.select_by_value("pretd")

    def expensive_product(self):
        assert self.is_displayed(locator=self.EXPENSIVE_LAPTOP)

    def cheapest_product(self):
        assert self.is_displayed(locator=self.CHEAPEST_PHONE)

    def expensive_christmas_tree(self):
        assert self.is_displayed(locator=self.EXPENSIVE_CHRISTMAS_TREE)

