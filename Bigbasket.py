from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

#<-------------------------------- For Chrome Browser --------------------------------------------->
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

#<-------------------------------- For Firefox ---------------------------------------------------->
# s=Service(GeckoDriverManager().install())
# driver = webdriver.Firefox(service=s)


#<--------------------------------- Maximize Window ------------------------------------------------>
driver.maximize_window()



try:
 driver.get("https://www.bigbasket.com/")
 print(driver.title)
 print(driver.current_url)
 driver.find_element(By.XPATH,".//input[@qa='searchBar']").send_keys("Tea")
 driver.find_element(By.XPATH,".//button[@qa='searchBtn']").click()
 driver.implicitly_wait(10)
finally:
  driver.back()
  driver.implicitly_wait(10)
  driver.refresh()
  driver.minimize_window()
  driver.close()

