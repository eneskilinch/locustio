from base.utils.chrome_browser import ChromeBrowser
from base.utils.settings import Settings, SettingKeys

settings = Settings()


class BaseTest(ChromeBrowser):
    driver = None
    url = None

    def __init__(self, *args, **kwargs):
        self.settings = Settings()
        ChromeBrowser.__init__(self, self.settings)
        self.driver = self.init_driver()
        if not self.url:
            self.url = self.settings.get(SettingKeys.TARGET_URL)
        self.driver.get(self.url)
