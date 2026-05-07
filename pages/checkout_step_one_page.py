from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutStepOnePage(BasePage):
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "[data-test='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "[data-test='lastName']")
    POSTAL_CODE_INPUT = (By.CSS_SELECTOR, "[data-test='postalCode']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-test='continue']")

    def is_loaded(self):
        return self.wait_for_text(self.TITLE, "Checkout: Your Information")

    def fill_form_and_continue(self, first_name, last_name, postal_code):
        self.type(self.FIRST_NAME_INPUT, first_name)
        self.type(self.LAST_NAME_INPUT, last_name)
        self.type(self.POSTAL_CODE_INPUT, postal_code)
        self.click(self.CONTINUE_BUTTON)
