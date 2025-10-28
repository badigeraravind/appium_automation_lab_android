import time
import random
from gesture_lab_apk.gesture_login import test_login_pass

def test_drag_drop(driver):
    a = driver.find_element('-android uiautomator','new UiSelector().className("android.view.View").instance(11)')
    driver.execute_script('mobile: clickGesture', {'elementId':a.id})

    for _ in range (1,11):
        b = driver.find_element('accessibility id','wooden_nail')
        src_x = random.randint(100,1000)
        src_y = random.randint(400, 2000)
        driver.execute_script('mobile: dragGesture',{'elementId':b.id, 'endX':src_x, 'endY':src_y, 'speed':1000})   #1000 pixels speed per second
        time.sleep(2)

