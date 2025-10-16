from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

def test_notif(driver):
    driver.open_notifications()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((AppiumBy.XPATH,'//android.widget.Toast[@text="New text message: r u hungry?  i am starved"]'))).click()
    #WebDriverWait(driver,10).until(EC.presence_of_element_located((AppiumBy.CLASS_NAME,"android.widget.Toast"))).click()


