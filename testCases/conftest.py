from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome('/Users/carl/Desktop/Q.A/chromedriver')
    return driver
