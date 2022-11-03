"""There is module which describe fixtures for WebDriver"""

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from browsers.browser_factory import WebDriversFactory


@pytest.fixture
def web_driver(pytestconfig) -> WebDriver:
    """
    This fixture provides to test WebDriver object and close them after test is finish.

    :return: WebDriver instances
    """
    web_driver = WebDriversFactory().get_web_driver(pytestconfig.getvalue("browser_name"))
    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()
