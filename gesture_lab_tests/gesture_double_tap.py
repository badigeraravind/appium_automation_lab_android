from gesture_lab_tests.gesture_login import test_login_pass
import time

def test_double_tap(driver):
    a = driver.find_element('accessibility id','nav_doubleTap')       
    driver.execute_script('mobile: clickGesture',{'elementId':a.id})                                                        # -> Tapping on the Double Tap option from the home screen
    time.sleep(3)

    b = driver.find_element('accessibility id','toy_idle')
    driver.execute_script('mobile: doubleClickGesture', {'elementId':b.id})
    print('Double tapped, toy is dancing')
    time.sleep(3)
    c = driver.find_element('accessibility id','toy_dancing')
    driver.execute_script('mobile: doubleClickGesture', {'elementId':b.id})
    print('Double tapped, toy is idle')




    