
import time
import random
from gesture_lab_tests.gesture_login import test_login_pass

def test_open_screen(driver):
    a = driver.find_element('-android uiautomator','new UiSelector().className("android.view.View").instance(13)')
    driver.execute_script('mobile: clickGesture', {'elementId':a.id}) #tapping on 'swipe/scoll' option

def test_swipe(driver):
    hor = driver.find_element('accessibility id','swipe_pager')
    for _ in [None] * 7:
        direction = random.choice(["left","right"])
        percent = round(random.uniform(0.3,0.7),2)
        driver.execute_script('mobile: swipeGesture',{'elementId':hor.id, 'direction':direction, 'percent':percent})
        print(f'\n<<< Swiped Horizontally in {direction} direction with {percent*100:.0f}% length >>>\n')
        time.sleep(3)
        

def test_scroll (driver):
    ver = driver.find_element('accessibility id','scroll_list')
    for _ in [None] * 5:
        direction = random.choice(["up","down"])
        percent = round(random.uniform(0.4,0.8),2)
        driver.execute_script('mobile: scrollGesture',{'elementId':ver.id, 'direction':direction, 'percent':percent})
        print(f'\n<<< Swiped Vertically in {direction} direction with {percent*100:.0f}% length >>>\n')
        time.sleep(3)
        





