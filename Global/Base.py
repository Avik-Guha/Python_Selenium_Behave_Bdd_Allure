import inspect
import time
from selenium import webdriver
from selenium.webdriver import Chrome, Firefox
import logging


def start_Browser_Driver(browser):
    global driver

    if str(browser) == "Chrome":
        chrome_driver_path = "Driver\\chromedriver.exe"
        driver = Chrome(executable_path=chrome_driver_path)
    elif str(browser) == "ChromeHeadless":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    elif str(browser) == "Firefox":
        firefox_driver_path = "Driver\\geckodriver.exe"
        driver = Firefox(executable_path=firefox_driver_path)
    else:
        chrome_driver_path = "Driver\\chromedriver.exe"
        driver = Chrome(executable_path=chrome_driver_path)

    driver.delete_all_cookies()
    driver.maximize_window()


def set_Env(environment):
    global Base_Url

    if str(environment) == "QA":
        Base_Url = "https://www.thetestingworld.com/testings/"
    elif str(environment) == "PROD":
        Base_Url = "https://www.thetestingworld.com/testings/PROD"
    else:
        Base_Url = "https://www.thetestingworld.com/testings/"


def set_Logger():
    global logger
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    handler_info = logging.FileHandler('Logs/info_log.txt')
    handler_info.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler_info.setFormatter(formatter)
    logger.addHandler(handler_info)

    return logger


def set_Driver(browser):
    start_Browser_Driver(browser)


def get_Driver():
    return driver


def set_Environment(environment):
    set_Env(environment)


def get_Environment():
    return Base_Url


def close_Browser():
    driver.quit()


def wait_for_seconds(seconds):
    time.sleep(seconds)
