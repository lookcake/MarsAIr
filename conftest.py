import pytest
import time
from selenium import webdriver
from pages.search_page import SearchPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.get("https://marsair.recruiting.thoughtworks.net/FanjieChen")
    driver.implicitly_wait(5)
    yield driver
    time.sleep(2)
    driver.quit()


@pytest.fixture
def search_page(driver):
    return SearchPage(driver)


