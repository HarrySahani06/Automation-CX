import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_cap = dict(
    deviceName='Android',
    platformName='Android',
    browserName='chrome'

)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
driver.get("http://google.com")
print(driver.title)
time.sleep(2)
driver.quit()
