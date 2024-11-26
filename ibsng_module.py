import global_variables as DB
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_driver():
    """
    creates a driver object and returns it
    """
    try:
        DB.IBSNG_DRIVER = webdriver.Firefox()
        DB.IBSNG_LOGGER_FILE.info('Driver Created Successfully')
    except Exception as e:
        DB.IBSNG_LOGGER_FILE.error(e.stacktrace[1])


def close_driver():
    DB.IBSNG_DRIVER.close()
    DB.IBSNG_LOGGER_FILE.info('Program Finished Successfully')


def login_into_page(username, password):

    try:
        DB.IBSNG_DRIVER.get(DB.IBSNG_LOGIN_URL_ADDRESS)
        time.sleep(3)

        username_input_xpath = '/html/body/table[3]/tbody/tr/td/form[1]/table/tbody/tr[3]/td[3]/input'
        WebDriverWait(DB.IBSNG_DRIVER, 10).until(
            EC.presence_of_element_located((By.XPATH, username_input_xpath)))

        username_input = DB.IBSNG_DRIVER.find_element(
            by=By.XPATH, value=username_input_xpath)
        username_input.send_keys(username)

        password_input_xpath = '/html/body/table[3]/tbody/tr/td/form[1]/table/tbody/tr[5]/td[3]/input'
        password_input = DB.IBSNG_DRIVER.find_element(
            by=By.XPATH, value=password_input_xpath)
        password_input.send_keys(password)

        login_btn_xpath = '/html/body/table[3]/tbody/tr/td/form[1]/table/tbody/tr[9]/td/table/tbody/tr[1]/td[3]/input'
        login_btn = WebDriverWait(DB.IBSNG_DRIVER, 10).until(
            EC.element_to_be_clickable((By.XPATH, login_btn_xpath)))
        login_btn.click()

        time.sleep(3)

        return True

    except Exception as e:
        DB.IBSNG_DRIVER.get(DB.IBSNG_LOGOUT_URL_ADDRESS)
        DB.IBSNG_LOGGER_FILE.info(
            f'Failed Login Attempt, username={username}, password={password}')
        # logger.error(e.stacktrace[1])
        return False


def user_traffic_exceeded():
    current_traffic_xpath = '/html/body/table[2]/tbody/tr/td/table[4]/tbody/tr[7]/td[3]'
    current_traffic_text = DB.IBSNG_DRIVER.find_element(
        by=By.XPATH, value=current_traffic_xpath).text

    match = re.search(DB.IBSNG_TRAFFIC_PATTERN, current_traffic_text)
    if match:
        current_traffic_num = int(match.group(1))

        if current_traffic_num > DB.IBSNG_TRAFFIC_LIMIT:
            return True

    return False
