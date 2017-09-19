from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Checkout:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)
        self.browser.implicitly_wait(1)

    def openCheckout(self):
        self.browser.find_element_by_css_selector("div#cart a:last-child").click()

    def removeProducts(self):
        product_number = self.browser.find_elements_by_css_selector("td.item")
        for c in product_number:
            table_item=self.browser.find_element_by_class_name("item")
            self.browser.find_element_by_name("remove_cart_item").click()
            WebDriverWait(self.browser, 10).until(EC.staleness_of(table_item))