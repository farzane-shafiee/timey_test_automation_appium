import time
from src.config.base_test import BaseTest
from src.config.base_test import SEARCH_INPUT_DATA_FILE_PATH
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.apps.page.login_compony_page.login_compony_page_action import LoginComponyPageAction
from src.apps.page.login_compony_page.gmail_api import get_otp_api


class TestLoginCompony(BaseTest):

    def test_01_welcome(self):
        login_compony_page = LoginComponyPageAction(driver=self.driver)

        self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, login_compony_page.locator['next_button'])
            )
        )

        login_compony_page.click_next_button()
        login_compony_page.click_next_button()
        login_compony_page.click_next_button()

    def test_02_login_compony_valid(self):
        login_compony_page = LoginComponyPageAction(driver=self.driver)

        data = self.read_data_device(SEARCH_INPUT_DATA_FILE_PATH)

        # self._01_welcome()

        login_compony_page.insert_username(data['username_input'])
        login_compony_page.click_submit_username_button()

        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, login_compony_page.locator['otp_page_label'])
            )
        )
        time.sleep(5)
        login_compony_page.insert_otp(get_otp_api())  # OTP
        login_compony_page.click_test_otp_button()


