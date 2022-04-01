import time
import os
from appium import webdriver
from Apps.Apkcode import APK

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.select import Select
app_obj = APK()
app_path = app_obj.CX_apk("1.31.10")
#app_path = app_obj.eleve_apk()
print(app_path)
# print(app_path)
desired_cap = dict(
    deviceName='Android',
    platformName='Android',
    app=app_path

)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)

time.sleep(2)
driver.quit()



