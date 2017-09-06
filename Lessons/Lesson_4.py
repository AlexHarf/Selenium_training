import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def is_element_present(driver, *args):
  try:
    driver.find_element(*args)
    return True
  except NoSuchElementException:
    return False



def test(driver):
    driver.implicitly_wait(10)
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_link_text("Appearence").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Template").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Logotype").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Catalog").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Product Groups").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Option Groups").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Manufacturers").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Suppliers").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Delivery Statuses").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Sold Out Statuses").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Quantity Units").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("CSV Import/Export").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Countries").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Currencies").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Customers").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("CSV Import/Export").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Newsletter").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Geo Zones").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Languages").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Storage Encoding").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Modules").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Customer").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Shipping").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Payment").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Order Total").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Order Success").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Order Action").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Orders").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Order Statuses").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Pages").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Reports").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Most Sold Products").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Most Shopping Customers").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Settings").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Defaults").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("General").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Listings").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Images").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Checkout").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Advanced").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Security").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Slides").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Tax").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Tax Rates").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Translations").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Scan Files").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("CSV Import/Export").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("Users").click()
    is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element_by_link_text("vQmods").click()
    is_element_present(driver, By.TAG_NAME, "h1")

