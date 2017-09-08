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
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    rows = driver.find_elements_by_css_selector(".dataTable .row td:nth-child(3)")
    print(rows)
    countries = []
    for row in rows:
        countries.append(row.text)
    for country in countries:
        driver.find_element_by_link_text(country).click()
        zones = driver.find_elements_by_css_selector(".dataTable tr td:nth-child(3) select option:checked")
        zoneName = ([p.text for p in zones])
        zoneNameOrder = zoneName
        zoneNameOrder.sort()
        if zoneName != zoneNameOrder:
            print(country)
            print("The order is incorrect.")
        else:
            print(country)
            print("The order is correct.")
        driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")