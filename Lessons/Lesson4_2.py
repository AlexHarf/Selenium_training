import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def are_elements_present(driver, *args):
    return len(driver.find_elements(*args)) = 1

def test(driver):
    driver.implicitly_wait(10)
    driver.get("http://localhost/litecart/")
    form = driver.find_element_by_id("box-most-popular")
    form.find_element_by_link_text("Green Duck")
    are_elements_present(driver, By.CLASS_NAME, "sticker new")
