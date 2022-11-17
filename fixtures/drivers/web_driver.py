"""There is module which describe fixtures for WebDriver"""

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from browsers.browser_factory import get_web_driver


@pytest.fixture
def web_driver() -> WebDriver:
    """
    This fixture provides to test WebDriver object and close them after test is finish.

    :return: WebDriver instances
    """
    web_driver = get_web_driver()
    yield web_driver
    web_driver.quit()
