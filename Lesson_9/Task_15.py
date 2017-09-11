import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = webdriver.Remote("http://192.168.1.35:4444/wd/hub", desired_capabilities={"browserName": "edge", "platform": "WIN10"})
    request.addfinalizer(wd.quit)
    return wd

def test(driver):
    driver.implicitly_wait(5)
    driver.get("http://software-testing.ru/")
    driver.find_element_by_id("pause")
