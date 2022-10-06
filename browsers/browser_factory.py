"""There is module which proved WebDriver instances base on browser name."""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from constants.taf_constants import BrowserName


class ChromeWebDriver:
    """Chrome WebDriver."""

    @staticmethod
    def get_service(self) -> WebDriver:
        """
        Starts the service and then creates new instance of chrome driver.

        :return: WebDriver for Chrome
        """
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


class FirefoxWebDriver:
    """FireFox WebDriver."""

    @staticmethod
    def get_service() -> WebDriver:
        """
        Starts the service and then creates new instance of firefox driver.

        :return: WebDriver for FireFox
        """
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


class EdgeWebDriver:
    """Edge WebDriver."""

    @staticmethod
    def get_service() -> WebDriver:
        """
        Starts the service and then creates new instance of edge driver.

        :return: WebDriver for Edge
        """
        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


class WebDriversFactory:
    """Collect knows WebDriver for browsers."""

    browsers = {
        BrowserName.CHROME: ChromeWebDriver(),
        BrowserName.FIREFOX: FirefoxWebDriver(),
        BrowserName.EDGE: EdgeWebDriver()
    }

    def get_web_driver(self, browser_name: str) -> WebDriver:
        """Provide WebDriver object by specify browser e.g. for FireFox, Chrome, Edge"""
        return self.browsers.get(browser_name).get_service()
