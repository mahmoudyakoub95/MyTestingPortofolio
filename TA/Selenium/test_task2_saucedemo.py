import time
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("username", [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user",
])
def test_login(driver, username):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    if username == "locked_out_user":
        assert "locked out" in driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    else:
        assert driver.find_element(By.CLASS_NAME, "title").text == "Products"
