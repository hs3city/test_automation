"""
There are module with fixtures for UI testing.
"""
import json
import string
from dataclasses import dataclass
from random import choice

import names
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from main import Constants


@dataclass
class User:
    """The simple data class for User."""
    first_name: str
    last_name: str
    email: str
    password: str


@pytest.fixture
def generate_password() -> str:
    """Generate password with ten letters, ten digits and ten punctuation e.g. KkQkIGmsVx1530668957(|+$,_('~{"""
    return "".join(choice(string.ascii_letters) for i in range(10)) + \
           "".join(choice(string.digits) for i in range(10)) + \
           "".join(choice(string.punctuation) for i in range(10))


@pytest.fixture(scope='session')
def config():
  with open('tests/config.json') as config_file:
    data = json.load(config_file)
  return data

@pytest.fixture
def web_driver(config) -> WebDriver:
    """
    This fixture provides to test WebDriver object and close them after test is finish.

    :return: WebDriver instances
    """
    if config['browser'] == 'firefox':
       driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', options=webdriver.FirefoxOptions())
    elif config['browser'] == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif config['browser'] == 'chromium':
        driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    elif config['browser'] == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    driver.maximize_window()
    driver.implicitly_wait(Constants.IMPLICITLY_WAIT)
    driver.get(Constants.MAIN_URL)
    yield driver
    driver.quit()


@pytest.fixture
def create_user_with_credentials(generate_password: str):
    """
    Generate new user with credentials.

    :return: User object
    """
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    email = f"{first_name}.{last_name}@gmail.com"
    return User(first_name, last_name, email, generate_password)


@pytest.fixture
def get_default_user():
    """
    Return user with has been registered on the system.

    :return: User object
    """
    return User("Ronald", "Longley", "Ronald.Longley@gmail.com", "QWERTY1234567890!@#$")


@pytest.fixture(autouse=False)
def login_user(web_driver, get_default_user):
    user = get_default_user
    web_driver.find_element(*Constants.ACCOUNT_BUTTON).click()
    web_driver.find_element(*Constants.USERNAME_INPUT_LOG).send_keys(user.email)
    web_driver.find_element(*Constants.PASSWORD_INPUT_LOG).send_keys(user.password)
    web_driver.find_element(*Constants.LOGIN_BUTTON).click()
