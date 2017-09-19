
import pytest
from selenium import webdriver
from product_select import ProductSelect
from product import Product
from checkout import Checkout

@pytest.fixture

def setUp(self):
    self.browser = webdriver.Chrome()
    self.select_product = ProductSelect(self.browser)
    self.product = Product(self.browser)
    self.checkout = Checkout(self.browser)
    self.addCleanup(self.browser.quit)

def test_All(self):
    self.select_product.open()
    self.select_product.Select()
    self.product.AddProduct()
    self.select_product.open()
    self.select_product.Select()
    self.product.AddProduct()
    self.select_product.open()
    self.select_product.Select()
    self.product.AddProduct()
    self.checkout_product.openCheckout()
    self.checkout_product.removeProducts()





