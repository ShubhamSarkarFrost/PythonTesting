import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# <-------------------------------- For Chrome Browser --------------------------------------------->
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, chrome_options=chrome_options)
driver.implicitly_wait(5)

# <-------------------------------- For Firefox ---------------------------------------------------->
# s = Service(GeckoDriverManager().install())
# driver = webdriver.Firefox(service=s)
# driver.implicitly_wait(5)

# <--------------------------------- Maximize Window ------------------------------------------------>
driver.maximize_window()

try:
    driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
    action = ActionChains(driver)
    action.double_click(driver.find_element(By.ID, "double-click")).perform()
    alert = driver.switch_to.alert
    time.sleep(2)
    assert "You double clicked me!!!, You got to be kidding me" == alert.text
    alert.accept()
    action.context_click(driver.find_element(By.NAME,"upload")).perform()
    time.sleep(3)
finally:
    driver.close()
