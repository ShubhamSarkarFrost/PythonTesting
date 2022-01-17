# to run the class it is py.test -k indigo -v -s
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


def test_searchflight():


    try:
        # <-------------------------------- For Chrome Browser --------------------------------------------->
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s, chrome_options=chrome_options)
        driver.implicitly_wait(6)

        # <-------------------------------- For Firefox ---------------------------------------------------->
        # firefox_option = webdriver.FirefoxOptions()
        # prefs = {"profile.default_content_setting_values.notifications" : 2}
        # s=Service(GeckoDriverManager().install())
        # driver = webdriver.Firefox(service=s , firefox_option =firefox_option)
        driver.maximize_window()
        driver.get("https://www.goindigo.in/")
    finally:
        driver.minimize_window()
        driver.close()