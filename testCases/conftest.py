from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup():
    # driver = webdriver.Chrome('/Users/carl/Desktop/Q.A/chromedriver')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

