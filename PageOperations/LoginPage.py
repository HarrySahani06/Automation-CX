from appium.webdriver.common.appiumby import AppiumBy
from Resources.base  import Base
from Page_object.login_page import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

class OtpOps:
    obj_OTP=OTP_info()
    def insert_otp(self, driver,wait):
        '''
        Inserts OTP
        '''
        otp_digit_xpath = self.obj_OTP.inputOTP()

        # 1st box
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, otp_digit_xpath[0])))
        driver.find_element(AppiumBy.XPATH, otp_digit_xpath[0]).send_keys('7')

        # 2st box
        driver.find_element(AppiumBy.XPATH,otp_digit_xpath[1]).send_keys('6')

        # 3rd box
        driver.find_element(AppiumBy.XPATH, otp_digit_xpath[2]).send_keys('5')

        # 4th box
        driver.find_element(AppiumBy.XPATH,otp_digit_xpath[3]).send_keys('6')


    def clickOtpContinue(self, driver,wait):
        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, self.obj_OTP.OtpContinue())))
        driver.find_element(AppiumBy.XPATH, self.obj_OTP.OtpContinue()).click()
