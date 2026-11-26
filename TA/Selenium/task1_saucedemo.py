from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start Chrome and open the shop.
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Find the login fields by their HTML id and type the test credentials.
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Check that the product page and the requested product are shown.
time.sleep(2)
assert driver.find_element(By.CLASS_NAME, "title").text == "Products"
assert driver.find_element(By.CLASS_NAME, "inventory_item_name").text == "Sauce Labs Backpack"

# Close Chrome when the checks are finished.
driver.quit()
