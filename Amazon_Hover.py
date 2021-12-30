import time
import json

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
driver.implicitly_wait(6)

# <--------------------------------- Maximize Window ------------------------------------------------>
driver.maximize_window()

try:
    driver.get("https://www.amazon.com")
    action = ActionChains(driver)
    menu = driver.find_element(By.XPATH, ".//span[@class='nav-line-2 ']")
    action.move_to_element(menu).perform()
    signin_button = driver.find_element(By.XPATH, "(.//span[@class='nav-action-inner'])[1]")
    action.move_to_element(signin_button).click().perform()
    time.sleep(4)
    with open('data.json', 'r') as myfile:
        data = myfile.read()
        obj = json.loads(data)

    email = str(obj['email'])
    password = str(obj['password'])
    driver.find_element(By.XPATH,".//input[@id='ap_email']").send_keys(email)
    driver.find_element(By.ID,"continue").click()
    driver.find_element(By.NAME,"password").send_keys(password)
    driver.find_element(By.NAME,"rememberMe").click()
    driver.find_element(By.ID,"signInSubmit").click()
    time.sleep(5)
    user = driver.find_element(By.XPATH,".//div[@class='nav-line-1-container']/span").text
    if user.__contains__("shubham"):
        print("User Logged In")
    else:
        print("User is not logged IN")

finally:
    driver.minimize_window()
driver.close()
