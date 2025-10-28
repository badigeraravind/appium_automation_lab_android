import time
from gesture_lab_apk.gesture_login import test_login_pass

def _test_internet(driver):
    a = driver.find_element('-android uiautomator','new UiSelector().className("android.view.View").instance(15)')
    driver.execute_script('mobile: clickGesture', {'elementId':a.id})
    time.sleep(5)
    driver.execute_script('mobile: setConnectivity', {'wifi':False, 'data': False, 'airplaneMode':False})
    time.sleep(5)
    driver.execute_script('mobile: setConnectivity', {'wifi':True, 'data': False})
    time.sleep(5)
    driver.execute_script('mobile: setConnectivity', {'wifi':False, 'data': False, 'airplaneMode':False})
    time.sleep(5)
    driver.execute_script('mobile: setConnectivity', {'wifi':False, 'data': True})

def test_bg_switch(driver):
    a = driver.find_element('-android uiautomator','new UiSelector().className("android.view.View").instance(15)')
    driver.execute_script('mobile: clickGesture', {'elementId':a.id})
    time.sleep(5)
    driver.press_keycode(3) 
    time.sleep(3)
    driver.activate_app('com.example.gesturelab')
    time.sleep(3)
    driver.background_app(5)
    driver.activate_app('com.google.android.calendar')
    time.sleep(5)
    driver.activate_app('com.example.gesturelab')
   

    

