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
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(5)

# <-------------------------------- For Firefox ---------------------------------------------------->
# s=Service(GeckoDriverManager().install())
# driver = webdriver.Firefox(service=s)


# <--------------------------------- Maximize Window ------------------------------------------------>
driver.maximize_window()

try:
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    products =driver.find_elements(By.XPATH,".//button[text()='ADD TO CART']")
    buttons = len(products)
    for button in range(0,4):
        products[button].click()
    driver.find_element(By.XPATH,".//img[@alt='Cart']").click()
    driver.find_element(By.XPATH,".//button[text()='PROCEED TO CHECKOUT']").click()
    # wait = WebDriverWait(driver, 5)
    # wait.until(EC.presence_of_element_located(By.CLASS_NAME,"promoCode"))
    driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
    driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
    promo_code = driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text
    print(promo_code)

finally:
    driver.close()