import os
import configparser


class Settings:
    project_name = "locustio"

    def get_project_dir(self):
        current_path_split = os.path.realpath(__file__).split(os.sep)
        last_project_name_index = len(current_path_split) - 1 - current_path_split[::-1].index(self.project_name)
        return os.path.join(os.sep.join(current_path_split[:last_project_name_index + 1]))

    def read_settings(self):
        ini_file_location = os.path.join(self.get_project_dir(), "base", "utils", "settings.ini")
        config = configparser.ConfigParser()
        config.read(ini_file_location, encoding='utf-8')
        settings = {}
        ini_env = "ALL"

        for option in config.options(ini_env):
            settings[option] = config.get(ini_env, option)

        for setting, value in settings.items():
            if value == "None":
                settings[setting] = None
        return settings

    def get(self, settings_key):
        settings = self.read_settings()
        return settings[settings_key]


class SettingKeys(enumerate):
    TARGET_URL = "target_url"
    TOKEN = "token"
    SESSION = "session"
    HEADLESS_MODE = "headless_mode"
    CHROMEDRIVER_PATH = "chromedriver_path"
    USER_AGENT = "user_agent"
    COOKIE_TOKEN_NAME = "cookie_token_name"
    COOKIE_SESSION_NAME = "cookie_session_name"
    COOKIE_DOMAIN = "cookie_domain"
