import time
from gesture_lab_tests.gesture_login import test_login_pass


def test_open_screen(driver):
    a = driver.find_element('accessibility id','nav_multiTouch')
    driver.execute_script('mobile: clickGesture', {'elementId': a.id})
    time.sleep(3)

def test_zoom_out(driver):
    b = driver.find_element('accessibility id','world_map')
    print("element rect:", b.rect)
    driver.execute_script(
        'mobile: pinchCloseGesture',
        {
            "elementId":b.id,
            'percent': 0.50,
            'speed': 300
        }
    )
time.sleep(3)
def test_zoom_in(driver):
    b = driver.find_element('accessibility id','world_map')
    print("element rect:", b.rect)
    driver.execute_script(
        'mobile: pinchOpenGesture',
        {
            "elementId":b.id,
            'percent': 0.80,
            'speed': 300
        }
    )

