import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(firefox_binary="c:\\Program Files\\Nightly\\firefox.exe")
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test(driver):
    driver.implicitly_wait(5)
    driver.get("http://localhost/litecart/en/")
    l = driver.find_element_by_css_selector("div#box-campaigns li.product.column.shadow.hover-light")

    name = l.find_element_by_css_selector(".name").get_attribute("textContent")
    priceReg = l.find_element_by_css_selector(".regular-price").get_attribute("textContent")
    priceRegSize = l.find_element_by_css_selector(".regular-price").value_of_css_property("font-size")
    priceRegColor = l.find_element_by_css_selector(".regular-price").value_of_css_property("color")
    assert priceRegColor == 'rgb(119, 119, 119)'
    priceRegType = l.find_element_by_css_selector(".regular-price").value_of_css_property("text-decoration-line")
    assert priceRegType == 'line-through'
    priceSale = l.find_element_by_css_selector(".campaign-price").get_attribute("textContent")
    priceSaleSize = l.find_element_by_css_selector(".campaign-price").value_of_css_property("font-size")
    assert priceSaleSize > priceRegSize
    priceSaleColor = l.find_element_by_css_selector(".campaign-price").value_of_css_property("color")
    assert priceSaleColor == 'rgb(204, 0, 0)'
    priceSaleType = l.find_element_by_css_selector(".campaign-price").value_of_css_property("font-weight")
    assert priceSaleType == '900'

    driver.find_element_by_xpath("//div[@id='box-campaigns']//li[1]").click()

    secName = driver.find_element_by_css_selector("h1.title").get_attribute("textContent")
    secPriceReg = driver.find_element_by_css_selector(".regular-price").get_attribute("textContent")
    secPriceRegSize = driver.find_element_by_css_selector(".regular-price").value_of_css_property("font-size")
    secPriceRegColor = driver.find_element_by_css_selector(".regular-price").value_of_css_property("color")
    assert secPriceRegColor == 'rgb(102, 102, 102)'
    secPriceRegType = driver.find_element_by_css_selector(".regular-price").value_of_css_property("text-decoration-line")
    assert secPriceRegType == 'line-through'
    secPriceSale = driver.find_element_by_css_selector(".campaign-price").get_attribute("textContent")
    secPriceSaleSize = driver.find_element_by_css_selector(".campaign-price").value_of_css_property("font-size")
    assert secPriceSaleSize > secPriceRegSize
    secPriceSaleColor = driver.find_element_by_css_selector(".campaign-price").value_of_css_property("color")
    assert secPriceSaleColor == 'rgb(204, 0, 0)'
    secPriceSaleType = driver.find_element_by_css_selector(".campaign-price").value_of_css_property("font-weight")
    assert secPriceSaleType == '700'

    assert name == secName
    assert priceReg == secPriceReg
    assert priceSale == secPriceSale

    # print(name)
    # print(priceReg)
    # print(priceRegSize)
    #print(priceRegColor)
    # print(priceRegType)
    # print(priceSale)
    # print(priceSaleSize)
    #print(priceSaleColor)
    #print(priceSaleType)
    #print(secName)
    #print(secPriceReg)
    #print(secPriceRegSize)
    #print(secPriceRegColor)
    #print(secPriceRegType)
    #print(secPriceSale)
    #print(secPriceSaleSize)
    #print(secPriceSaleColor)
    #print(secPriceSaleType)
