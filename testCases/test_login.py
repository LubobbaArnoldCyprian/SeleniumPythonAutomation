import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from testCases.conftest import setup
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        #self.logger.INFO("***** Test_001_Login *****")
        #self.logger.INFO("**** Verifying Home Page Title *****")
        self.driver = setup
        #self.logger.INFO("***** Test_001_Login *****")
        self.driver.get(self.baseURL)
        #self.logger.INFO("**** Verifying Home Page Title *****")
        act_title = self.driver.title
        print(act_title)
        if act_title != "Your store. Login":
            self.driver.save_screenshot(".//Screenshots/"+"self.test_homePageTitle.png")
            self.logger.error("**** Home page title test is failed ****")
            self.driver.close()
            assert False
        else:
            assert True
        self.driver.close()

    def test_login(self, setup):
        #self.logger.INFO("**** verifying Login page ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        #self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            #self.logger.INFO("**** login test is passed ****")
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots/" + "self.test_homePageTitle.png")
            #self.logger.error("**** login test is failed ****")
            self.driver.close()
            assert False

