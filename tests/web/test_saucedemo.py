import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage

class TestSauceDemo:
    @pytest.fixture(autouse=True)
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--window-size=1920,1080")
        
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1920, 1080)
        
        yield
        
        self.driver.quit()

    def test_fluxo_checkout_completo(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(self.driver)
        assert inventory_page.is_loaded(), "A lista de produtos não foi carregada com sucesso."
        
        inventory_page.add_backpack_to_cart()
        assert inventory_page.get_cart_item_count() == 1
        
        inventory_page.open_cart()

        cart_page = CartPage(self.driver)
        assert cart_page.is_loaded()
        assert cart_page.get_number_of_items() == 1
        cart_page.proceed_to_checkout()

        checkout_one = CheckoutStepOnePage(self.driver)
        assert checkout_one.is_loaded()
        checkout_one.fill_form_and_continue("Eduardo", "QA", "12345-678")

        checkout_two = CheckoutStepTwoPage(self.driver)
        assert checkout_two.is_loaded()
        checkout_two.finish_checkout()

        checkout_complete = CheckoutCompletePage(self.driver)
        assert checkout_complete.is_loaded()
        assert checkout_complete.get_success_message() == "Thank you for your order!", "A mensagem de sucesso final está incorreta ou não apareceu!"
