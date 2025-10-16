# Ensures imports like `from utils...` work no matter where pytest runs from
# import os, sys
# ROOT = os.path.dirname(os.path.abspath(__file__))
# if ROOT not in sys.path:
#    sys.path.insert(0, ROOT)



# conftest.py
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options  # <-- NEW

@pytest.fixture

def driver():
    caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "emulator-5554",  # or your adb device name
    #   "appPackage": "io.appium.android.apis",
    #   "appActivity": ".ApiDemos",
        "appPackage": "com.example.gesturelab",
        "appActivity": ".GestureLabActivity",
        "noReset": True,
        "newCommandTimeout": 180,
        "adbExecTimeout": 120000,
        "uiautomator2ServerLaunchTimeout": 60000,
        "disableWindowAnimation": False,
        "autoGrantPermissions": True,
        "ignoreHiddenApiPolicyError": True,
        "chromedriverExecutable": r"C:\Users\arvba\Downloads\chromedriver_win32\chromedriver.exe"
    }
    
    options = UiAutomator2Options().load_capabilities(caps)           # Build an Options object from caps (required by Selenium/Appium now)

    drv = webdriver.Remote("http://127.0.0.1:4723",options = options) # pass options=
    yield drv
    drv.quit()
