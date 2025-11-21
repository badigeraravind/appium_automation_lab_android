import time
from gesture_lab_apk.gesture_login import test_login_pass

def test_internet(driver):
    a = driver.find_element('-android uiautomator','new UiSelector().className("android.view.View").instance(15)')
    driver.execute_script('mobile: clickGesture', {'elementId':a.id})
    time.sleep(5)
    driver.execute_script('mobile: setConnectivity', {'wifi':False, 'data': False, 'airplaneMode':False})
    time.sleep(5)
    driver.execute_script('mobile: setConnectivity', {'wifi':False, 'data': True})


   

    

