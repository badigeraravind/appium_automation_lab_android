#scroll

def test_scroll(driver):
    a = driver.find_element(by = "accessibility id", value = "App")
    a.click()

    b = driver.find_element(by = "accessibility id", value = "Activity")
    b.click()

    c = driver.find_element(by = '-android uiautomator', value = 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Wallpaper"))')
    c.click()

