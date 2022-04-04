
from appium.webdriver.common.appiumby import AppiumBy
from Page_object.Logo_Page import logo_Page
from selenium.webdriver.support.ui import WebDriverWait
from Resources.base import Base
from selenium.webdriver.support import  expected_conditions as EC


class logo_operations:

    def operation(self, driver,wait):
        # # Press continue button at the beginning
        logoPage = logo_Page()
        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,logoPage.get_continue_button())))
        driver.find_element(AppiumBy.XPATH,logoPage.get_continue_button()).click()




