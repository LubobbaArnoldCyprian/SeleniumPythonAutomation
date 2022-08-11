import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from testCases.conftest import setup
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        print(act_title)
        if act_title != "Your store. Login1":
            self.driver.save_screenshot(".//Screenshots/"+"self.test_homePageTitle.png")
            self.driver.close()
            assert False
        else:
            assert True
        self.driver.close()


    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False
