#single tap gesture

# from appium.webdriver.common.touch_action import TouchAction  >> This doesn't work in latest appium versions

def test_touch_gesture(driver):

    a = driver.find_element(by="accessibility id", value = "Preference")
    driver.execute_script("mobile: clickGesture", {"elementId":a.id})
    # TouchAction(driver).tap(a).perform()

    b = driver.find_element(by="accessibility id", value = "9. Switch")
    driver.execute_script("mobile: clickGesture", {"elementId":b.id})
    # TouchAction(driver).tap(b).perform()

    c = driver.find_elements(by="class name", value="android.widget.RelativeLayout")

    for j in c:
        driver.execute_script("mobile: clickGesture", {"elementId":j.id})
        #TouchAction(driver).tap(j).perform()



