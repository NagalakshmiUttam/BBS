from pageobjects.login_page import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import pytest
import time

class CommonLogin():
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()

    email=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    def __init__(self, setup):
        self.driver=setup

    def common_login(self): # we remove setup from here and create a new constructor above to initiate setup method in other classes
        self.logger.info("*** starting test_001_login***")
        # self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        lp=LoginPage(self.driver)
        lp.setEmail(self.email)
        lp.setPW(self.password)
        lp.clickLogin()
        time.sleep(2)


        targetText=lp.isTextExists()
        if targetText==True:
            assert True
        else:
            self.driver.save_screenshot("C:\\Nagalakshmi\\PythonPractice\\BPMT\\screenshots\\test_001_failed.png")
            assert False

        # self.driver.close()
        self.logger.info("***End of the test_001_login***")
           
        