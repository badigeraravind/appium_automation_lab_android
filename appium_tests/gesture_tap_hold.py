import time
from appium_tests.gesture_login import test_login_pass

def test_tap_hold(driver):
    a = driver.find_element('-android uiautomator','new UiSelector().className("android.view.View").instance(9)')
    driver.execute_script('mobile: clickGesture',{'elementId':a.id})
    time.sleep(3)

    b = driver.find_element('accessibility id','btn_preview')
    driver.execute_script('mobile: longClickGesture',{'elementId':b.id, 'duration':8000})
