import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options  # <-- NEW

@pytest.fixture

def driver():
    appium_url = os.getenv("APPIUM_SERVER_URL") or "http://127.0.0.1:4723"

    # If running in CI and no remote Appium is configured, skip the tests
    if os.getenv("GITHUB_ACTIONS") and not os.getenv("APPIUM_SERVER_URL"):
        pytest.skip("No APPIUM_SERVER_URL configured in CI. Set repo secret or run locally.", allow_module_level=True)
        
    caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": os.getenv("DEVICE_NAME", "emulator-5554"),  # or your adb device name
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
        #"chromedriverExecutable": r"C:\Users\arvba\Downloads\chromedriver_win32\chromedriver.exe"
    }

    # Add chromedriver path only when provided (avoids Windows-only hardcoded path in CI)
    chromedriver_env = os.getenv("CHROMEDRIVER_PATH")
    if chromedriver_env:
        caps["chromedriverExecutable"] = chromedriver_env
    
    options = UiAutomator2Options().load_capabilities(caps)           # Build an Options object from caps (required by Selenium/Appium now)

    drv = webdriver.Remote(appium_url, options = options) # pass options=
    yield drv
    drv.quit()
