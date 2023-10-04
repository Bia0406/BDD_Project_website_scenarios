from selenium.webdriver.common.by import By

from base_page import BasePage


class LoginPage(BasePage):
    LOGIN_PAGE = f"{BasePage._BASE_URL}/index.php?main_page=login&cust=1"
    EMAIL_BTN = (By.ID, "email_address")
    PASSWORD_BTN = (By.NAME, "passwordx")
    CONNECT_BTN = (By.CLASS_NAME, "btnSubmit")
    COOKIES_BTN = (By.XPATH, "//a[text()='Accept']")
    ERROR_MSG = (By.CLASS_NAME, "eroareafis")

    def navigate_to_login_page(self):
        self.browser.get(self.LOGIN_PAGE)

    def insert_email(self, email):
        self.insert(locator=self.EMAIL_BTN, text=email)

    def insert_any_password(self):
        self.insert(locator=self.PASSWORD_BTN, text="123456")

    def insert_valid_password(self):
        self.insert(locator=self.PASSWORD_BTN, text="bia0406")

    def click_login_button(self):
        self.click(locator=self.CONNECT_BTN)

    def click_cookies_button(self):
        self.click(locator=self.COOKIES_BTN)

    def error_msg_is_displayed(self):
        assert self.is_displayed(locator=self.ERROR_MSG)

