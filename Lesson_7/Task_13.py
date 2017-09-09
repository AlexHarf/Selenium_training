import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test(driver):
    driver.implicitly_wait(5)
    driver.get("http://localhost/litecart/en/")

    for i in range(0, 3):
        menu = driver.find_elements_by_css_selector("div#box-most-popular.box a:not([data-fancybox-group])")
        menu[i].click()
        size = driver.find_elements_by_name("options[Size]")
        if len(size) > 0:
            size_select = Select(driver.find_element_by_name('options[Size]'))
            size_select.select_by_value('Small')
        driver.find_element_by_name("add_cart_product").click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div#cart span.quantity"), str(i+1)))
        driver.get("http://localhost/litecart/en/")

    driver.find_element_by_css_selector("div#cart a:last-child").click()
    product_number = driver.find_elements_by_css_selector("td.item")
    for c in product_number:
        table_item=driver.find_element_by_class_name("item")
        driver.find_element_by_name("remove_cart_item").click()
        WebDriverWait(driver, 10).until(EC.staleness_of(table_item))








    #driver.find_element_by_name("date_valid_to").send_keys("11112020")