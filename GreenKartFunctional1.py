import collections


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
    products = driver.find_elements(By.XPATH, ".//button[text()='ADD TO CART']")
    productname = driver.find_elements(By.XPATH, ".//h4[@class='product-name']")
    buttons = len(products)
    product_list = []
    for button in range(0, 4):
        products[button].click()
        product_list.append(productname[button].text)

    print(product_list)
    driver.find_element(By.XPATH, ".//img[@alt='Cart']").click()
    driver.find_element(By.XPATH, ".//button[text()='PROCEED TO CHECKOUT']").click()
    cartproduct_list = []
    cart_list = driver.find_elements(By.XPATH, ".//p[@class='product-name']")
    products = len(cart_list)

    for cart in range(0, 4):
        cartproduct_list.append(cart_list[cart].text)

    print(cartproduct_list)
    if collections.Counter(product_list) == collections.Counter(cartproduct_list):
        print("Two Lists are Identical")
    else:
        print("Two Lists are not identical")
    total_amt = int(driver.find_element(By.XPATH, ".//span[@class='totAmt']").text)
    driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
    driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
    promo_code = driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text
    print(promo_code)
    discount_text = driver.find_element(By.XPATH,".//span[@class='discountPerc']").text
    discount_per = int(discount_text[0:2])
    discount_amount = (total_amt * discount_per) / 100
    discount_price = total_amt - discount_amount
    actual_price = int(driver.find_element(By.XPATH,".//span[@class='discountAmt']").text)
    assert actual_price == discount_price




finally:
    driver.minimize_window()
    driver.close()
