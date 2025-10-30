#click and back

def test_menu_list(driver):
    menu = driver.find_elements(by="id", value = "android:id/text1")
    
    for i, j in enumerate(menu, start=1):
        print(f"#{i} === {j.text}")

    menu[2].click()
    driver.back()

def test_open_animation(driver):
    menu = driver.find_element(by = '-android uiautomator', value = 'new UiSelector().text("Animation")')
    menu.click()
    
