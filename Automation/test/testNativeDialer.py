import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy



desired_cap = dict(
    deviceName='Android',
    platformName='Android',
    appPackage = 'com.android.contacts',
    appActivity ='com.oppo.contacts.activities.OppoContactsTabActivity'

)

#to grep app package andd activity name
# make sure  device is connected to adb devices
# now hit comand adb shell
# open native app/ hybrid app
# and in shell hit command - dumpsys window windows|grep -E 'mTopActivityComponent'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)


driver.quit()
