from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    my_account_xpath = "//span[normalize-space()='My Account']"
    login_button_linktext = "Login"
    register_button_linktext = "Register"
    search_box_xpath = "//input[@placeholder='Search']"
    search_button_xpath = "//i[@class='fa fa-search']"

    def search_box_element(self, product_name):
        self.driver.find_element(By.XPATH, self.search_box_xpath).send_keys(product_name)

    def search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()

    def click_on_my_account(self):
        self.driver.find_element(By.XPATH, self.my_account_xpath).click()

    def click_on_login_button(self):
        self.driver.find_element(By.LINK_TEXT, self.login_button_linktext).click()

    def click_on_register(self):
        self.driver.find_element(By.LINK_TEXT, self.register_button_linktext).click()

    def click_on_myaccount_than_login(self):
        self.click_on_my_account()
        self.click_on_login_button()

    def click_on_myaccount_than_register(self):
        self.click_on_my_account()
        self.click_on_register()

