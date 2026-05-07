from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutStepTwoPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    FINISH_BUTTON = (By.CSS_SELECTOR, "[data-test='finish']")

    def is_loaded(self):
        return self.get_text(self.TITLE) == "Checkout: Overview"
        
    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)
