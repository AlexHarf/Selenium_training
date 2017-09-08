import pytest
from selenium import webdriver

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
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    links = driver.find_elements_by_css_selector("table.dataTable a:not([title])")
    countries = [g.get_attribute("innerText") for g in links]
    countriesOrder = countries
    countriesOrder.sort()
    if countries != countriesOrder:
        print("The order of countries is incorrect.")
    else:
        print("The order of countries is correct.")

def test_zones(driver):
    driver.implicitly_wait(5)
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    zoneCountries = []
    rows = driver.find_elements_by_css_selector(".row")
    for i in rows:
        if '0' != i.find_element_by_css_selector("td:nth-child(6)").get_attribute("textContent"):
            zoneCountries.append(i.find_element_by_css_selector("td:nth-child(4)").get_attribute("textContent"))
    for c in zoneCountries:
        driver.get("http://localhost/litecart/admin/?app=countries&doc=edit_country&country_code=%s" % c)
        zones = driver.find_elements_by_css_selector("table#table-zones td:nth-child(3)")
        zoneName = ([p.text for p in zones])
        zoneNameOrder = zoneName
        zoneNameOrder.sort()
        if zoneName != zoneNameOrder:
            print (c)
            print ("The order is incorrect.")
        else:
            print(c)
            print("The order is correct.")
