import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import random

email = 'test%s@mail.ru' % (str(random.randint(0, 99)))

form = {'email': email}

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test(driver):
    driver.implicitly_wait(5)
    driver.get("http://localhost/litecart/en/create_account")
    driver.find_element_by_name("firstname").send_keys("FirstNameIsHere")
    driver.find_element_by_name("lastname").send_keys("LastNameIsHere")
    driver.find_element_by_name("address1").send_keys("AddressIsHere")
    driver.find_element_by_name("postcode").send_keys("12345")
    driver.find_element_by_name("city").send_keys("TheCityIsHere")

    country_select = Select(driver.find_element_by_name('country_code'))
    country_select.select_by_value('US')
    state_select = Select(driver.find_element_by_css_selector('select[name=zone_code]'))
    state_select.select_by_value('AK')

    driver.find_element_by_name("email").send_keys(form['email'])
    driver.find_element_by_name("phone").send_keys("+16478327649")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("confirmed_password").send_keys("admin")

    driver.find_element_by_name("create_account").click()
    driver.find_element_by_link_text("Logout").click()

    driver.find_element_by_name("email").send_keys(form['email'])
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_link_text("Logout").click()








