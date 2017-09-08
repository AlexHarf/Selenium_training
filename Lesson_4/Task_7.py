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
    menu = driver.find_elements_by_css_selector("li#app- a")
    for i in range(len(menu)):
        menuitem = driver.find_elements_by_css_selector("li#app-")
        menuitem[i].click()
        assert len(driver.find_elements_by_tag_name('h1')) == 1
        submenu = driver.find_elements_by_css_selector("li[id^=doc]")
        if len(submenu) > 0:
            for j in range(len(submenu)):
                submenuitem = driver.find_elements_by_css_selector("li[id^=doc] a")
                submenuitem[j].click()
                assert len(driver.find_elements_by_tag_name('h1')) == 1