import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    browser = webdriver.Chrome()  # Start Chrome for one test.
    yield browser                # Give Chrome to the test.
    browser.quit()               # Close Chrome after the test.
