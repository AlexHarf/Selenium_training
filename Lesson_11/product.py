from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Product:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)
        self.browser.implicitly_wait(1)

    def AddProduct(self):
        size = self.browser.find_elements_by_name("options[Size]")
        if len(size) > 0:
            size_select = Select(self.browser.find_element_by_name('options[Size]'))
            size_select.select_by_value('Small')
            self.browser.find_element_by_name("add_cart_product").click()
        WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div#cart span.quantity"), str(i + 1)))
