from dotenv import load_dotenv
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from src.config.conftest import ConfigTest

SEARCH_INPUT_DATA_FILE_PATH = "src/device_data/input_data.yml"
DEVICE_DATA_FILE_PATH = "src/device_data/data_device.yml"


class BaseTest(ConfigTest):
    driver = None
    wait = None

    @classmethod
    def setup_class(cls):
        """
        Remote and connect to device_data.
        """
        load_dotenv()
        cls.initialize_mysql_manager()
        # print(cls.read_data_device(DEVICE_DATA_FILE_PATH))
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", cls.read_data_device(DEVICE_DATA_FILE_PATH))

        cls.driver.implicitly_wait(5)
        cls.wait = WebDriverWait(cls.driver, 10)

    # @classmethod
    # def teardown_class(cls):
    #     cls.mysql_manager.close_connection()
