from random import choice

from locust import HttpUser, between, task

from base.authenticator_helper import *
from base.base_functions import Base
from base.base_test import *

settings = Settings()


class WebsiteUser(HttpUser, BaseTest, Base):
    wait_time = between(5, 15)
    url = settings.get(SettingKeys.TARGET_URL)

    def on_start(self):
        """
        Adds given cookies from settings.ini file to the driver to be logged into panel
        Loads cookies from driver and headers from settings.ini file to http.client
        Goes to target url and collects all requests from network and quits driver

        """
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get(self.url)
        for cookie in self.driver.get_cookies():
            self.client.cookies.set(cookie['name'], cookie['value'])
        self.client.headers.update(header)
        network = self.get_network_requests(timeout=5)
        self.href_list = self.filter_collected_network(network, internal=True)
        self.driver.quit()

    @task(5)
    def newsletter_do_list(self):
        """
        Random checks the request that collected from network of chromedriver

        """
        url = choice(self.href_list)
        r = self.client.get(url)
        print(r.content)    # check if content comes as an User
