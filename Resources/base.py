from appium import webdriver
from Apps.Apkcode import APK


class Base:

    def instantiate_driver(self):
        app_obj = APK()
        app_path = app_obj.CX_apk("1.31.10")
        desired_cap = {
            "deviceName": 'Android',
            "platformName": "Android",
            "app": app_path,
            "noReset": "false",
            "fullReset": "false",
            "newCommandTimeout": "600000",
            # "enforceAppInstall":"false",
            # "autoLaunch":"false",
            "appium:appPackage": "live.citymall.customer.prod",
            "appium:appActivity": "live.citymall.customer.MainActivity",
            # "appium:app": "C:\\Users\\admin\\Downloads\\live.citymall.customer.prod_2022-02-10.apk",
            # "appium:deviceName": "",
            "appium:automationName": "UiAutomator2"}

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        return driver



