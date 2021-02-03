from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from decouple import config

USERNAME = config("USERNAME")
PASSWORD = config("PASSWORD")


driver = webdriver.Chrome()
driver.get(
    "https://www.bestbuy.com/site/apple-airpods-pro-white/5706659.p?skuId=5706659"
)
# elem = driver.find_element_by_xpath(
#     "//*[@data-sku-id='5706659']")

elem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@data-sku-id='5706659']"))
)
elem.click()

driver.get("https://www.bestbuy.com/cart")
elem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "checkout-buttons__checkout"))
)
elem.click()


email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "fld-e"))
)
email.click()
email.send_keys(USERNAME)

password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "fld-p1"))
)
password.click()
password.send_keys(PASSWORD)
