import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test(driver):
    driver.get("http://localhost/litecart/")
    ducks = driver.find_elements_by_class_name("product")
    for i in range (len(ducks)):
        assert len(ducks[i].find_elements_by_class_name("sticker")) == 1
