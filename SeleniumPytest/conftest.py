import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def setup():
    # <-------------------------------- For Chrome Browser --------------------------------------------->
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, chrome_options=chrome_options)
    driver.implicitly_wait(6)
    driver.maximize_window()
    driver.get("https://www.goindigo.in/")

    # <-------------------------------- For Firefox ---------------------------------------------------->
    # firefox_option = webdriver.FirefoxOptions()
    # prefs = {"profile.default_content_setting_values.notifications" : 2}
    # s=Service(GeckoDriverManager().install())
    # driver = webdriver.Firefox(service=s , firefox_option =firefox_option)

    yield
    driver.minimize_window()
    driver.close()