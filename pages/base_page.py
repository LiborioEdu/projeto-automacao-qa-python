from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_text(self, locator, text):
        # Aguarda ativamente o texto mudar, de forma Case-Insensitive.
        # Chrome Headless em CI pode retornar upper-case dependendo do CSS text-transform.
        try:
            def _text_match_case_insensitive(driver):
                elements = driver.find_elements(*locator)
                if not elements:
                    return False
                return text.lower() in elements[0].text.lower()
            return self.wait.until(_text_match_case_insensitive)
        except:
            return False
