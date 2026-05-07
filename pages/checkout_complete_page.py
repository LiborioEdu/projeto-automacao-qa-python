from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    COMPLETE_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")

    def is_loaded(self):
        return self.wait_for_text(self.TITLE, "Checkout: Complete!")
        
    def get_success_message(self):
        return self.get_text(self.COMPLETE_HEADER)
