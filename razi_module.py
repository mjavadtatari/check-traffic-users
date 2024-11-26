import global_variables as DB
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_driver():
    """
    creates a driver object and returns it
    """
    try:
        DB.RAZI_DRIVER = webdriver.Firefox()
        DB.RAZI_LOGGER_FILE.info('Driver Created Successfully')
    except Exception as e:
        DB.RAZI_LOGGER_FILE.error(e.stacktrace[1])


def close_driver():
    DB.RAZI_DRIVER.close()
    DB.RAZI_LOGGER_FILE.info('Program Finished Successfully')


def log_in_user(username, password):

    try:
        DB.RAZI_DRIVER.get(DB.RAZI_LOGIN_URL_ADDRESS)
        time.sleep(3)

        username_input_xpath = '//*[@id="username"]'
        WebDriverWait(DB.RAZI_DRIVER, 10).until(
            EC.presence_of_element_located((By.XPATH, username_input_xpath)))

        username_input = DB.RAZI_DRIVER.find_element(
            by=By.XPATH, value=username_input_xpath)
        username_input.send_keys(username)

        password_input_xpath = '//*[@id="password"]'
        password_input = DB.RAZI_DRIVER.find_element(
            by=By.XPATH, value=password_input_xpath)
        password_input.send_keys(password)

        login_btn_xpath = '//*[@id="login"]/div[3]/button'
        login_btn = WebDriverWait(DB.RAZI_DRIVER, 10).until(
            EC.element_to_be_clickable((By.XPATH, login_btn_xpath)))
        login_btn.click()

        time.sleep(3)

        return True

    except Exception as e:
        DB.RAZI_DRIVER.get(DB.RAZI_LOGOUT_URL_ADDRESS)
        DB.RAZI_LOGGER_FILE.info(
            f'Failed Login Attempt, username={username}, password={password}')
        # logger.error(e.stacktrace[1])
        return False
