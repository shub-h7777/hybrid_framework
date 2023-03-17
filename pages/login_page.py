from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.NAME, "username").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, "password").send_keys(password)

    def click_on_login(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

    @property
    def get_invalid_error_message(self):
        return self.driver.find_element(By.XPATH, "//p[text()='Invalid credentials']").text

    @property
    def get_username_placeholder(self):
        return self.driver.find_element(By.NAME, "username").get_attributes("placeholder")

    @property
    def get_password_placeholder(self):
        return self.driver.find_element(By.NAME, "password").get_attributes("placeholder")