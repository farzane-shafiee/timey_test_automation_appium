from selenium.webdriver.common.by import By
from src.apps.page.login_compony_page.login_compony_page_locators import LoginComponyPageLocators


class LoginComponyPageAction:
    """
    All my reports page tests operations are in this class.
    """
    def __init__(self, driver):
        self.driver = driver
        self.locator = LoginComponyPageLocators()

    def click_next_button(self):
        self.driver.find_element(By.ID, self.locator['next_button']).click()

    def insert_username(self, username):
        self.driver.find_element(By.ID, self.locator['username_input']).send_keys(username)

    def click_submit_username_button(self):
        self.driver.find_element(By.ID, self.locator['submit_username_button']).click()

    def insert_otp(self, otp_input):
        self.driver.find_element(By.ID, self.locator['otp_input']).send_keys(otp_input)

    def click_test_otp_button(self):
        self.driver.find_element(By.ID, self.locator['test_otp_button']).click()
    # def my_reports_list(self):
    #     if self.driver.find_elements(By.XPATH, self.locator['my_reports_list']):
    #         element = self.driver.find_elements(By.XPATH, self.locator['my_reports_list'])
    #         return element
    #     else:
    #         return ""