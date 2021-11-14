import time

from base.utils.settings import Settings, SettingKeys


class Base(object):
    """
    Page class that all page models can inherit from

    """

    def __init__(self, driver):
        """
        Inits Selenium Driver class with driver
        :param driver: WebDriver instance

        """
        self.driver = driver

    def driver(self):
        return self.driver

    def get_network_requests(self, timeout=10):
        """
        Gets and returns all file type requests in network
        :params int timeout: Seconds to make wait driver

        """
        time.sleep(timeout)
        return self.driver.execute_script(
            "var network = window.performance.getEntries() || {}; return network;")

    @staticmethod
    def filter_collected_network(network, is_filter=False, initiator_type=None, internal=False, external=False):
        """
        Filters collected network request with given initiator type
        :params list network: A list of network requests
        :params bool is_filter: True if want to filter by initiator type
        :params bool internal: True if want to collect only internal request
        :params bool external: True if want to collect only external request
        :params str initiator_type: List of Initiator type:["link", "script", "css", "first-paint", "xmlhttprequest",
                                                            "img", "other", "first-contentful-paint", "use", "fetch"]

        """
        target_url = Settings().get(SettingKeys.TARGET_URL)
        filtered_request = []
        for request in network:
            try:
                if is_filter and request["initiatorType"] == initiator_type:
                    filtered_request.append(request["name"])
                elif not is_filter and not internal:
                    filtered_request.append(request["name"])
                elif internal and target_url in request["name"]:
                    filtered_request.append(request["name"])
                elif external and target_url not in request["name"]:
                    filtered_request.append(request["name"])
            except KeyError:
                pass
        return filtered_request
