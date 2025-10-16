
#tap and hold (long press)

def test_tap_hold_gesture(driver):
    a = driver.find_element(by="accessibility id",value="Media")
    driver.execute_script("mobile: clickGesture",{"elementId":a.id})

    b = driver.find_element(by="accessibility id", value="AudioFx")
    driver.execute_script("mobile: clickGesture",{"elementId":b.id})

    driver.execute_script("mobile: longClickGesture", {"x":150, "y":786, "duration":5000})

    driver.execute_script ("mobile: longClickGesture", {"x":226, "y":990, "duration":3000})


