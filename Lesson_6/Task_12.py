import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import os

img = os.path.normpath(os.path.join(os.getcwd(), "the_duck.jpg"))

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test(driver):
    driver.implicitly_wait(5)
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
    driver.find_element_by_css_selector("#content a.button:last-child").click()

    driver.find_element_by_name("name[en]").send_keys("NewProductName")
    name = ("NewProductName")
    driver.find_element_by_name("code").send_keys("12345")
    driver.find_element_by_name("quantity").clear()
    driver.find_element_by_name("quantity").send_keys("100")
    driver.find_element_by_name("new_images[]").send_keys(img)
    driver.find_element_by_name("date_valid_from").send_keys("11112016")
    driver.find_element_by_name("date_valid_to").send_keys("11112020")

    menu = driver.find_elements_by_css_selector("div.tabs li")
    menu[1].click()

    manufacturer_select = Select(driver.find_element_by_name('manufacturer_id'))
    manufacturer_select.select_by_value('1')

    driver.find_element_by_name("keywords").send_keys("keyword")
    driver.find_element_by_name("short_description[en]").send_keys("shortDescription")
    driver.find_element_by_class_name("trumbowyg-editor").send_keys("fullDescription")
    driver.find_element_by_name("head_title[en]").send_keys("productTitle")

    menu = driver.find_elements_by_css_selector("div.tabs li")
    menu[3].click()

    driver.find_element_by_name("purchase_price").clear()
    driver.find_element_by_name("purchase_price").send_keys("50")

    currency_select = Select(driver.find_element_by_name('purchase_price_currency_code'))
    currency_select.select_by_value('USD')

    driver.find_element_by_name("save").click()

    products = driver.find_elements_by_css_selector("table.dataTable tr.row td a")
    if not (name in [product.text for product in products]):
        print("The product not found")
    else:
        print("The product added successfully")
