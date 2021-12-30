import collections
import time


from selenium import webdriver
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
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, chrome_options=chrome_options)
driver.implicitly_wait(5)

# <-------------------------------- For Firefox ---------------------------------------------------->
# firefox_option = webdriver.FirefoxOptions()
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# s=Service(GeckoDriverManager().install())
# driver = webdriver.Firefox(service=s , firefox_option =firefox_option)


# <--------------------------------- Maximize Window ------------------------------------------------>
driver.maximize_window()

try:
    driver.get("https://www.axisbank.com/")
    # <-------- close the Apply Now Option --------------------------->
    closebutton = driver.find_element(By.XPATH,"(.//div[@class='close_button'])[1]")
    if closebutton.is_displayed():
        closebutton.click()
        driver.find_element(By.XPATH, "(.//div[@class='reportFraudFtr']/a)[1]").click()
    else:
    #<------------------- Click on Apply fraud Button ------------------------------>
      driver.find_element(By.XPATH,"(.//div[@class='reportFraudFtr']/a)[1]").click()
    time.sleep(4)
    parent_window = driver.window_handles[0]
    child_window = driver.window_handles[1]
    driver.switch_to.window(child_window)
    time.sleep(4)
    fraud_text = driver.find_element(By.ID,"ContentPlaceHolder1_ucsubissue1_lblIssue").text
    assert fraud_text == "How do I report a fraudulent transaction"
    driver.switch_to.new_window(parent_window)


finally:
    driver.minimize_window()
    driver.close()
