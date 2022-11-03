"""There is module which proved WebDriver instances base on browser name."""
import os

from selenium import webdriver

from constants.taf_constants import BrowserName


def get_chrome_web_driver():
    return webdriver.Chrome()


def get_chrome_options():
    return webdriver.ChromeOptions()


def get_firefox_web_driver():
    return webdriver.Firefox()


def get_firefox_options():
    return webdriver.FirefoxOptions()


def get_edge_web_driver():
    return webdriver.Edge()


def get_edge_options():
    return webdriver.EdgeOptions()


def get_local_web_driver_generator(browser):
    web_driver_mapping = {
        BrowserName.CHROME: get_chrome_web_driver,
        BrowserName.FIREFOX: get_firefox_web_driver,
        BrowserName.EDGE: get_edge_web_driver,
    }
    web_driver_generator = web_driver_mapping.get(browser)
    return web_driver_generator


def get_remote_web_driver_options(browser):
    web_driver_options_mapping = {
        BrowserName.CHROME: get_chrome_options(),
        BrowserName.EDGE: get_edge_options(),
        BrowserName.FIREFOX: get_firefox_options(),
    }
    web_driver = web_driver_options_mapping.get(browser)
    return web_driver


def set_web_driver_options(web_driver):
    web_driver.maximize_window()
    wait_time = os.environ.get("WAIT_TIME", 2.0)
    web_driver.implicitly_wait(wait_time)
    main_url = os.environ.get("MAIN_URL", "http://skleptest.pl/")
    web_driver.get(main_url)


def get_web_driver():
    selenium_grid_url = os.environ.get("SELENIUM_GRID_URL")
    browser = os.environ.get("BROWSER", BrowserName.CHROME)

    if not selenium_grid_url:
        web_driver_generator = get_local_web_driver_generator(browser)
        web_driver = web_driver_generator()
    else:
        web_driver_options = get_remote_web_driver_options(browser)
        web_driver = webdriver.Remote(
            command_executor=selenium_grid_url,
            options=web_driver_options,
        )

    if not web_driver:
        raise ValueError(f"Browser {browser} does not exist")

    set_web_driver_options(web_driver)

    return web_driver
