import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(by, value)
    def after_find(self, by, value, driver):
        print(by, value, "found")
    def on_exception(self, exception, driver):
        print(exception)

@pytest.fixture
def driver(request):
    wd = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.implicitly_wait(5)
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    first_menu = driver.find_elements_by_css_selector("li#app-")
    first_menu[1].click()
    second_menu = driver.find_elements_by_css_selector("tr.row")
    second_menu[1].find_element_by_css_selector("a").click()
    items = driver.find_elements_by_css_selector('td:nth-child(3)>a[href*=\'product_id\']')
    urls = []
    for item in items:
        urls.append(item.get_attribute('href'))
    for url in urls:
        logs = driver.get_log('browser')
        driver.get(url)
        print(logs)
        assert len(logs) == 0
