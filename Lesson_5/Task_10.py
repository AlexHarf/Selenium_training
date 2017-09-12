import pytest
from selenium import webdriver
import ast

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test(driver):
    regList = []
    saleList = []

    driver.implicitly_wait(5)
    driver.get("http://localhost/litecart/en/")
    l = driver.find_element_by_css_selector("div#box-campaigns li.product.column.shadow.hover-light")

    name = l.find_element_by_css_selector(".name").get_attribute("textContent")
    priceReg = l.find_element_by_css_selector(".regular-price").get_attribute("textContent")
    priceRegSize = l.find_element_by_css_selector(".regular-price").value_of_css_property("font-size")
    priceRegColor = l.find_element_by_css_selector(".regular-price").value_of_css_property("color")
    regList.append(priceRegColor)
    priceRegType = l.find_element_by_css_selector(".regular-price").value_of_css_property("text-decoration-line")
    assert priceRegType == '' or 'line-through'
    priceSale = l.find_element_by_css_selector(".campaign-price").get_attribute("textContent")
    priceSaleSize = l.find_element_by_css_selector(".campaign-price").value_of_css_property("font-size")
    assert priceSaleSize > priceRegSize
    priceSaleColor = l.find_element_by_css_selector(".campaign-price").value_of_css_property("color")
    saleList.append(priceSaleColor)
    priceSaleType = l.find_element_by_css_selector(".campaign-price").value_of_css_property("font-weight")
    assert priceSaleType == 'bold' or '900'

    driver.find_element_by_xpath("//div[@id='box-campaigns']//li[1]").click()

    secName = driver.find_element_by_css_selector("h1.title").get_attribute("textContent")
    secPriceReg = driver.find_element_by_css_selector(".regular-price").get_attribute("textContent")
    secPriceRegSize = driver.find_element_by_css_selector(".regular-price").value_of_css_property("font-size")
    secPriceRegColor = driver.find_element_by_css_selector(".regular-price").value_of_css_property("color")
    regList.append(secPriceRegColor)
    secPriceRegType = driver.find_element_by_css_selector(".regular-price").value_of_css_property("text-decoration-line")
    assert secPriceRegType == '' or 'line-through'
    secPriceSale = driver.find_element_by_css_selector(".campaign-price").get_attribute("textContent")
    secPriceSaleSize = driver.find_element_by_css_selector(".campaign-price").value_of_css_property("font-size")
    assert secPriceSaleSize > secPriceRegSize
    secPriceSaleColor = driver.find_element_by_css_selector(".campaign-price").value_of_css_property("color")
    saleList.append(secPriceSaleColor)
    secPriceSaleType = driver.find_element_by_css_selector(".campaign-price").value_of_css_property("font-weight")
    assert secPriceSaleType == 'bold' or '900'

    assert name == secName
    assert priceReg == secPriceReg
    assert priceSale == secPriceSale

    browserName = driver.capabilities['browserName']
    for i in regList:
        if browserName == ("chrome"):
            r, g, b, alpha = ast.literal_eval(i.strip("rgba"))
            assert r == g
            assert r == b
        else:
            r, g, b = ast.literal_eval(i.strip("rgb"))
            assert r == g
            assert r == b

    browserName = driver.capabilities['browserName']
    for p in saleList:
        if browserName == ("chrome"):
            r, g, b, alpha = ast.literal_eval(p.strip("rgba"))
            assert g == 0
            assert b == 0
        else:
            r, g, b = ast.literal_eval(p.strip("rgb"))
            assert g == 0
            assert b == 0
