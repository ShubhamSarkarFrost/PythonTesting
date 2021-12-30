import collections
import time


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# <-------------------------------- For Chrome Browser --------------------------------------------->
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(5)

# <-------------------------------- For Firefox ---------------------------------------------------->
# s=Service(GeckoDriverManager().install())
# driver = webdriver.Firefox(service=s)

try:
    driver.get("https://the-internet.herokuapp.com/iframe")
    driver.maximize_window()
    #<------- Pass Frame ID or Index Value -------------------------->
    driver.switch_to.frame("mce_0_ifr")
    editor = driver.find_element(By.CSS_SELECTOR,"#tinymce")
    editor.send_keys(Keys.DELETE)
    driver.find_element(By.CSS_SELECTOR,"#tinymce").send_keys("Hi There Shubham Here")
    time.sleep(4)

finally:
    driver.minimize_window()
    driver.close()