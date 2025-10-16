
from appium import webdriver


def test_open_accessibility(driver):
    driver.implicitly_wait(5)
    a = driver.find_element(by="accessibility id", value="Accessibility")
    a.click()

    b = driver.find_element(by="accessibility id",value="Accessibility Node Provider")
    assert b.is_displayed()

