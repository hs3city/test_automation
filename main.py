"""
There is a simple script to automate test cases.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Constants:
    """
    This class provides constants for WebDriver to find something elements.
    """
    IMPLICITLY_WAIT = 2.0
    MAIN_URL = "http://skleptest.pl/"
    ACCOUNT_BUTTON = (By.XPATH, "//li[@class='top-account']")
    
    LOGIN_BUTTON = (By.XPATH, "//input[@name='login']")
    REG_BUTTON = (By.XPATH, "//input[@class='woocommerce-Button button' and @name='register']")
    
    USERNAME_INPUT_LOG = (By.XPATH, "//input[@id='username']")
    PASSWORD_INPUT_LOG = (By.XPATH, "//input[@id='password']")
    
    ERROR_MESSAGE = (By.XPATH, "//ul[@class='woocommerce-error']")
    HELLO_MESSAGE = (By.XPATH, "//div[@class='woocommerce-MyAccount-content']")
    
    EMAIL_INPUT_REG = (By.XPATH, "//input[@id='reg_email']")
    PASSWORD_INPUT_REG = (By.XPATH, "//input[@id='reg_password']")
    
    REG_LABEL = (By.XPATH, "//h2[contains(text(),'Register')]")


class ErrorMessageText:
    """
    This class provides Error text messages.
    """
    USERNAME_REQUIREMENT = "Error: Username is required."
    PASSWORD_EMPTY = "ERROR: The password field is empty."


def test_empty_username_and_password(web_driver: WebDriver):
    """
    Test case:
    1. Click account button on the http://skleptest.pl/ page.
    2. Username and password are empty in login form.
    3. Click Login button.
    4. Check that error message text equals "Error: Username is required."

    :param web_driver: WebDriver object
    """
    web_driver.find_element(*Constants.ACCOUNT_BUTTON).click()
    web_driver.find_element(*Constants.LOGIN_BUTTON).click()
    text_message = web_driver.find_element(*Constants.ERROR_MESSAGE).text
    assert text_message == ErrorMessageText.USERNAME_REQUIREMENT


def test_empty_password(web_driver: WebDriver):
    """
    Test case:
    1. Click account button on the http://skleptest.pl/ page.
    2. Input username in login form.
    3. Password field is empty in login form.
    4. Click Login button.
    5. Check that error message text equals "ERROR: The password field is empty."

    :param web_driver: WebDriver object
    """
    web_driver.find_element(*Constants.ACCOUNT_BUTTON).click()
    web_driver.find_element(*Constants.USERNAME_INPUT_LOG).send_keys("username")
    web_driver.find_element(*Constants.LOGIN_BUTTON).click()
    text_message = web_driver.find_element(*Constants.ERROR_MESSAGE).text
    assert text_message == ErrorMessageText.PASSWORD_EMPTY


def test_user_registration(web_driver: WebDriver, create_user_with_credentials):
    """
    Test case:
    1. Click account button on the http://skleptest.pl/ page.
    2. Input email in registration form.
    3. Input password in registration form.
    4. Click Register button.
    5. Check that first and last name present in hello message text.

    :param web_driver: WebDriver object
    :param create_user_with_credentials: User object
    """
    user = create_user_with_credentials
    web_driver.find_element(*Constants.ACCOUNT_BUTTON).click()
    web_driver.find_element(*Constants.EMAIL_INPUT_REG).send_keys(user.email)
    web_driver.find_element(*Constants.PASSWORD_INPUT_REG).send_keys(user.password)
    web_driver.find_element(*Constants.REG_LABEL).click()
    WebDriverWait(web_driver, 30).until(EC.element_to_be_clickable(Constants.REG_BUTTON))
    web_driver.find_element(*Constants.REG_BUTTON).click()
    WebDriverWait(web_driver, 30).until(EC.presence_of_element_located(Constants.HELLO_MESSAGE))
    hello_message = web_driver.find_element(*Constants.HELLO_MESSAGE).text
    assert user.first_name and user.last_name in hello_message, \
        f"{user.first_name} and {user.last_name} does not present in {hello_message}"


def test_user_login(web_driver: WebDriver, get_default_user, login_user):
    """
    Test case:
    1. Click account button on the http://skleptest.pl/ page.
    2. Input email in login form.
    3. Input password in login form.
    4. Click Login button.
    5. Check that first and last name present in hello message text.

    :param web_driver: WebDriver object
    :param get_default_user: User object
    """
    user = get_default_user
    WebDriverWait(web_driver, 30).until(EC.presence_of_element_located(Constants.HELLO_MESSAGE))
    hello_message = web_driver.find_element(*Constants.HELLO_MESSAGE).text
    assert user.first_name and user.last_name in hello_message, \
        f"{user.first_name} and {user.last_name} does not present in {hello_message}"


def test_add_item_to_cart(web_driver: WebDriver, login_user):
    web_driver.get(Constants.MAIN_URL)
    product = "Little Black Top"
    add_to_cart_button = web_driver.find_element(By.XPATH, f"//*[normalize-space() = '{product}']//..//a")
    #add_to_cart_button = web_driver.find_element(By.XPATH, "//a[@data-product_id='17']") - alternative way of search
    add_to_cart_button.click()
    cart_button = web_driver.find_element(By.XPATH, f'//*/li[@class="top-cart"]/a')
    cart_button.click()
    #to refactor - write better xpath and handle multiple items in the cart
    card_item = web_driver.find_element(By.XPATH, f'//*[@id="post-6"]/div[2]/form/table/tbody/tr[1]/td[@class="product-name"]/a').text
    assert product in card_item

