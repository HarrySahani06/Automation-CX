from appium.webdriver.common.appiumby import AppiumBy
import Resources.base as bs
from Page_object.OTP_Page import OTP_info
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC



class Otp_operation:

    OTP_obj= OTP_info()

    def insert_number(self, driver,wait):
        '''
        Inserts Number to get OTP
        '''
        wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, self.OTP_obj.inputNumberXpath())))
        driver.find_element(AppiumBy.XPATH, self.OTP_obj.inputNumberXpath()).send_keys(self.OTP_obj.input_number())


    def clickGetOtp(self, driver,wait):
        '''
        Click Get OTP button
        '''
        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, self.OTP_obj.getOtpXpath())))
        driver.find_element(AppiumBy.XPATH, self.OTP_obj.getOtpXpath()).click()


