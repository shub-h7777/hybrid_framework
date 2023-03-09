import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.webdriver_listner import WebDriverWrapper
from utilities import data_source


class TestAddEmployee(WebDriverWrapper):

    @pytest.mark.parametrize(
        "username, password, firstname, middlename, lastname, expected_profile_name,expected_firstname",
        data_source.test_add_valid_employee_data
    )
    def test_add_valid_employee(self, username, password, firstname, middlename, lastname, expected_profile_name,
                                expected_firstname):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.driver.find_element(By.LINK_TEXT, "PIM").click()
        self.driver.find_element(By.XPATH, "//a[text()='Add Employee']").click()
        self.driver.find_element(By.NAME, "firstName").send_keys(firstname)
        self.driver.find_element(By.NAME, "middleName").send_keys(middlename)
        self.driver.find_element(By.NAME, "lastName").send_keys(lastname)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        actual_profile_name = self.driver.find_element(By.XPATH,
                                                       f"//h6[contains(normalize-space(),'{firstname}')]").text
        actual_firstname = self.driver.find_element(By.NAME, "firstName").get_attribute("value")
        print(actual_firstname)
        assert_that(actual_profile_name).is_equal_to((expected_profile_name))
        assert_that(actual_firstname).is_equal_to(expected_firstname)
        # some time this assertion fails or sometime it pass for "PETER".
