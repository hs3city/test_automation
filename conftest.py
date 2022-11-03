"""
There are module with fixtures for UI testing.
"""
import string
from dataclasses import dataclass
from random import choice

import names
import pytest

from main import Constants

pytest_plugins = [
    "fixtures.drivers.web_driver",
]


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
