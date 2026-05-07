from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class InventoryPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    ADD_TO_CART_BACKPACK = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    def is_loaded(self):
        return self.wait_for_text(self.TITLE, "Products")

    def add_backpack_to_cart(self):
        self.click(self.ADD_TO_CART_BACKPACK)

    def get_cart_item_count(self):
        return int(self.get_text(self.CART_BADGE))

    def open_cart(self):
        # Utiliza JS Click para contornar problemas de Phantom Interception no Headless Mode
        # O badge ou child elements do SVG às vezes "engolem" o clique normal do Selenium na nuvem.
        element = self.wait.until(EC.presence_of_element_located(self.CART_LINK))
        self.driver.execute_script("arguments[0].click();", element)
