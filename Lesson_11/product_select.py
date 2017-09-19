class ProductSelect:
    def __init__(self, browser):
        self.browser = browser
        self.browser.implicitly_wait(1)

    def open(self):
        self.browser.get("http://localhost/litecart/en/")
        return self

    def Select(self):
        self.browser.find_elements_by_css_selector("div#box-most-popular.box a:not([data-fancybox-group])").click()