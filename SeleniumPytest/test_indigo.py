import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


def test_searchflight():
    # <-------------------------------- For Chrome Browser --------------------------------------------->
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    # <-------------------------------- For Firefox ---------------------------------------------------->
    # s=Service(GeckoDriverManager().install())
    # driver = webdriver.Firefox(service=s)

    # <--------------------------------- Maximize Window ------------------------------------------------>
    driver.maximize_window()

    try:
        driver.get("https://www.goindigo.in/")
    finally:
        driver.minimize_window()
        driver.close()
