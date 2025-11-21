from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from gesture_lab_tests.gesture_login import test_login_pass

def test_webview(driver):
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,'nav_webview_loading'))).click()

    print('\navailable contexts: ',driver.contexts)

    WebDriverWait(driver,10).until(EC.invisibility_of_element_located((AppiumBy.ACCESSIBILITY_ID,'webview_loading_screen')))

    b = driver.contexts
    print('\navailable contexts after loading screen: ',b)

    for ctx in b:
        if 'WEBVIEW' in ctx:
            driver.switch_to.context(ctx)
            print("Switched to:", ctx)
            break
    
    WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState')=='complete')       #waits for webpage to load completely

    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#login_field"))).send_keys("badigeraravinda@gmail.com")
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#password"))).send_keys("Arv@github798")
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"body > div.logged-out.env-production.page-responsive.session-authentication > div.application-main > main > div > div.authentication-body.authentication-body--with-form.new-session > form > div:nth-child(4) > input"))).click()
    print('Logged In to GITHUB Successfully')