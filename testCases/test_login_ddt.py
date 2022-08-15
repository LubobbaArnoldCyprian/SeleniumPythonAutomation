import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from testCases.conftest import setup
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    # username = ReadConfig.getUseremail()
    # password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        # self.logger.INFO("**** verifying Login page ****")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        XLUtils.getColumnCount(self.path, 'Sheet1')
        print("number of rows in the excel:", self.rows)
        list_status = []  # empty variable list

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("passed")
                    self.lp.clickLogout();
                    list_status.append("Pass")
                elif self.exp == "fail":
                    self.logger.info("*** failed***")
                    self.lp.clickLogout();
                    list_status.append("fail")
            elif act_title != exp_title:
                if self.exp == 'pass':
                    self.logger.info("*** failed***")
                    list_status.append("fail")
                elif self.exp == 'Fail':
                    self.logger.info("*** passed ***")
                    list_status.append("Pass")

        if "fail" not in list_status:
            self.logger.info("Login DDT test passed....")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT test failed....")
            self.driver.close()
            assert False

        self.logger.info("****end of ddt test*****")
        self.logger.info("*****Completed tc_ddt_002 successfully******")

