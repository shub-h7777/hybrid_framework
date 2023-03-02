from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginUI:
    def test_title(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        actual_title = driver.title
        assert_that("OrangeHRM").is_equal_to(actual_title)

    def test_header(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        header = driver.find_element(By.XPATH, "//h5").text
        assert_that("Login").is_equal_to(header)
