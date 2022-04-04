from Resources.base import Base as bs
from PageOperations.HomePage import *
from PageOperations.LoginPage import *
from PageOperations.LogoPage import *
from PageOperations.OtpPage import *
from selenium.webdriver.support import  expected_conditions as EC


class Login:
    base = Base()
    driver = base.instantiate_driver()
    wait = WebDriverWait(driver, 3)

    #instantiate all classes objects
    obj_OtpPage = Otp_operation()
    obj_LogoPage = logo_operations()
    obj_Login = OtpOps()

    '''
    Running Each method for automation operation
    '''

    obj_LogoPage.operation(driver,wait)

    #insertion of Mobile nUmber and moving forward
    obj_OtpPage.insert_number(driver,wait)
    obj_OtpPage.clickGetOtp(driver,wait)

    #insertion of OTP and movinf forward
    obj_Login.insert_otp(driver,wait)
    obj_Login.clickOtpContinue(driver, wait)







