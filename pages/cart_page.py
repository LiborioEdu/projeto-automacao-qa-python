from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    CART_ITEMS = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='checkout']")
    
    def is_loaded(self):
        return self.get_text(self.TITLE) == "Your Cart"

    def get_number_of_items(self):
        items = self.find_elements(self.CART_ITEMS)
        return len(items)

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
