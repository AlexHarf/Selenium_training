import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test(driver):
    wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(5)
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_css_selector("#content a.button:first-child").click()
    links = driver.find_elements_by_class_name("fa-external-link")
    for link in links:
        main_window = driver.current_window_handle
        old_windows = driver.window_handles
        link.click()
        wait.until(EC.number_of_windows_to_be(2))
        new_windows = driver.window_handles
        new_window = list(set(new_windows) - set(old_windows))[0]
        driver.switch_to_window(new_window)
        driver.close()
        driver.switch_to_window(main_window)
