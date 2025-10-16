
# character inputs into text fields

import time
import pytest

def _test_login_fail_retry (driver):
    uname = driver.find_element(by="accessibility id", value="username_field")
    pwd = driver.find_element(by="accessibility id", value="password_field")

    driver.execute_script("mobile: clickGesture", {"elementId":uname.id})                   
    driver.execute_script("mobile: type", {"elementId": uname.id, "text": "falsename"})

    driver.execute_script("mobile: clickGesture", {"elementId":pwd.id})                     
    driver.execute_script("mobile: type", {"elementId": pwd.id, "text": "false@902"})

    login_button = driver.find_element(by="class name", value="android.widget.Button")
    driver.execute_script("mobile: clickGesture", {"elementId":login_button.id})
    print('\ninvalid line to be shown\n')
    driver.back()

    time.sleep(3)

    driver.execute_script("mobile: clickGesture", {"elementId":uname.id})
    for _ in range(1,16):
        driver.press_keycode(67)   
    driver.execute_script("mobile: type", {"elementId": uname.id, "text": "truename"})


    driver.execute_script("mobile: clickGesture", {"elementId":pwd.id})
    for _ in range(1,16):
        driver.press_keycode(67)                      
    driver.execute_script("mobile: type", {"elementId": pwd.id, "text": "true@902"})

    login_button = driver.find_element(by="class name", value="android.widget.Button")
    driver.execute_script("mobile: clickGesture", {"elementId":login_button.id})


@pytest.mark.skip(reason="Tentative")
def test_login_fail (driver):
    uname = driver.find_element(by="accessibility id", value="username_field")
    pwd = driver.find_element(by="accessibility id", value="password_field")

    driver.execute_script("mobile: clickGesture", {"elementId":uname.id})                   
    driver.execute_script("mobile: type", {"elementId": uname.id, "text": "falsename"})

    driver.execute_script("mobile: clickGesture", {"elementId":pwd.id})                     
    driver.execute_script("mobile: type", {"elementId": pwd.id, "text": "false@902"})

    login_button = driver.find_element(by="class name", value="android.widget.Button")
    driver.execute_script("mobile: clickGesture", {"elementId":login_button.id})
    driver.back()

def test_login_pass (driver):
    uname = driver.find_element(by="accessibility id", value="username_field")
    pwd = driver.find_element(by="accessibility id", value="password_field")

    driver.execute_script("mobile: clickGesture", {"elementId":uname.id})                   
    driver.execute_script("mobile: type", {"elementId": uname.id, "text": "truename"})

    driver.execute_script("mobile: clickGesture", {"elementId":pwd.id})                     
    driver.execute_script("mobile: type", {"elementId": pwd.id, "text": "true@902"})

    login_button = driver.find_element(by="class name", value="android.widget.Button")
    driver.execute_script("mobile: clickGesture", {"elementId":login_button.id})