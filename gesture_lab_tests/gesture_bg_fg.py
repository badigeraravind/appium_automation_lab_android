import time
from gesture_lab_apk.gesture_login import test_login_pass

def test_bg_switch(driver):
    a = driver.find_element('-android uiautomator','new UiSelector().className("android.view.View").instance(15)')
    driver.execute_script('mobile: clickGesture', {'elementId':a.id})
    time.sleep(5)
    driver.press_keycode(3)             #method 1: android home button
    time.sleep(3)
    driver.activate_app('com.example.gesturelab')
    time.sleep(3)
    driver.background_app(5)            #method 2
    driver.activate_app('com.google.android.calendar')      #method 3
    time.sleep(5)
    driver.activate_app('com.example.gesturelab')