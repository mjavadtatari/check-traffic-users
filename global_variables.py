# isbng variables
IBSNG_DRIVER = ''
IBSNG_LOGIN_URL_ADDRESS = 'https://acc.razi.ac.ir/IBSng/user/'
IBSNG_HOME_URL_ADDRESS = 'https://acc.razi.ac.ir/IBSng/user/home.php'
IBSNG_LOGOUT_URL_ADDRESS = 'https://acc.razi.ac.ir/IBSng/user/?logout=1'
IBSNG_PASSWORD_CHANGE_URL_ADDRESS = 'https://acc.razi.ac.ir/IBSng/user/change_pass.php'
IBSNG_TRAFFIC_LIMIT = 5
IBSNG_TRAFFIC_PATTERN = r"^(\d+).*G"
IBSNG_SLEEP_TIME = 900  # 900 is 15 minutes
IBSNG_LOG_FILE_PATH = 'ibsng.log'
IBSNG_LOG_FORMAT = '[%(asctime)s] %(levelname)-9s %(name)-10s %(funcName)-30s %(message)s'
IBSNG_ALERT_TEXT = 'کاربر گرامی کلمه عبور شما منقضی شده است، لطفا به منظور تغییر کلمه عبور به حساب کاربری خود مراجه نمایید'
IBSNG_DEFAULT_PASSWORD = '9771413'
IBSNG_LOGGER_FILE = ''


# razi variables
RAZI_DRIVER = ''
RAZI_LOGIN_URL_ADDRESS = 'http://192.168.5.3/login'
RAZI_HOME_URL_ADDRESS = 'http://192.168.5.3/status'
RAZI_LOG_FILE_PATH = 'razi.log'
RAZI_LOG_FORMAT = '[%(asctime)s] %(levelname)-9s %(name)-10s %(funcName)-30s %(message)s'
RAZI_ALERT_TEXT = 'کاربر گرامی کلمه عبور شما منقضی شده است، لطفا به منظور تغییر کلمه عبور به حساب کاربری خود مراجه نمایید'
RAZI_DEFAULT_PASSWORD = '9771413'
RAZI_LOGGER_FILE = ''
