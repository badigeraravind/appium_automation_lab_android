import time
from gesture_lab_tests.gesture_login import test_login_pass

def test_single_tap(driver):
    a = driver.find_element('-android uiautomator','new UiSelector().className("android.view.View").instance(5)')
    driver.execute_script('mobile: clickGesture',{'elementId':a.id})
    time.sleep(3)
    b = driver.find_element('-android uiautomator','new UiSelector().className("android.widget.Button").instance(0)')
    driver.execute_script('mobile: clickGesture',{'elementId':b.id})
    print('\n\nLights are turned ON\n\n')
    time.sleep(3)
    driver.execute_script('mobile: clickGesture',{'elementId':b.id})
    print('\n\nLights are now turned OFF\n\n')

