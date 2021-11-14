import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from base.utils.settings import SettingKeys


class ChromeBrowser:
    def __init__(self, settings):
        """
        :param Settings settings:
        """
        self.settings = settings
        self.chrome_options = self.get_chrome_options()
        self.driver = None

    def get_webdriver_path(self):
        if self.settings.get(SettingKeys.CHROMEDRIVER_PATH):
            return self.settings.get(SettingKeys.CHROMEDRIVER_PATH)
        return os.path.join(
            self.settings.get_project_dir(), "base", "utils", "webdrivers", "chromedriver"
        )

    def get_chrome_options(self):
        chrome_options = Options()
        if self.settings.get(SettingKeys.HEADLESS_MODE) == "yes":
            chrome_options.add_argument("--headless")
        return chrome_options

    def init_driver(self):
        driver = webdriver.Chrome(
            executable_path=self.get_webdriver_path(), chrome_options=self.chrome_options
        )
        self.driver = driver
        driver.maximize_window()
        return driver
