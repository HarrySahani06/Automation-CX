import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.select import Select

desired_cap = dict(
    deviceName='Android',
    platformName='Android',
    browserName='chrome'

)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
driver.get("https://www.wikipedia.org")
print(driver.title)
dropdown=driver.find_element(AppiumBy.XPATH,'//div[@id="search-input"]/div/div/select')
select = Select(dropdown)
select.select_by_value("hi")
options = driver.find_element(AppiumBy.TAG_NAME,'option')
for var_options in options:
    print("Text is ",options.text," lang is ",options.get_attribute('lang'))
time.sleep(2)
driver.quit()
