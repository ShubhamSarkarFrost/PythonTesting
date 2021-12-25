from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# <-------------------------------- For Chrome Browser --------------------------------------------->
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

# <-------------------------------- For Firefox ---------------------------------------------------->
# s=Service(GeckoDriverManager().install())
# driver = webdriver.Firefox(service=s)


# <--------------------------------- Maximize Window ------------------------------------------------>
driver.maximize_window()

try:
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.find_element(By.XPATH, "(.//input[@name='name'])[1]").send_keys("Shubham Sarkar")
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "email").send_keys("subhampandora123@gmail.com")
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "exampleCheck1").click()
    driver.implicitly_wait(10)
    drop = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
    drop.select_by_visible_text("Female")
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "inlineRadio1").click()
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "bday").send_keys("08-08-1995")





finally:
    driver.refresh()
driver.minimize_window()
driver.close()
