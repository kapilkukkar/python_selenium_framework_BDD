from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    email_field_xpath = "//input[@id='input-email']"
    password_field_xpath = "//input[@id='input-password']"
    submit_button_xpath = "//input[@value='Login']"

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.email_field_xpath).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_field_xpath).send_keys(password)

    def click_submit_button(self):
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()

