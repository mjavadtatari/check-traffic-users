import global_variables as DB
import logger_module
import time
import get_data_from_csv
import ibsng_module
import razi_module


if __name__ == '__main__':
    DB.IBSNG_LOGGER_FILE = logger_module.create_logger(
        DB.IBSNG_LOG_FILE_PATH, DB.IBSNG_LOG_FORMAT)
    DB.RAZI_LOGGER_FILE = logger_module.create_logger(
        DB.RAZI_LOG_FILE_PATH, DB.RAZI_LOG_FORMAT)

    USERS_DATA = get_data_from_csv.get_data()['exported_list']
    tmp_user = [USERS_DATA[0], USERS_DATA[26]]

    ibsng_module.create_driver()
    razi_module.create_driver()

    for user in tmp_user:
        if ibsng_module.login_into_page(user[1], user[0]):

            while not ibsng_module.user_traffic_exceeded():
                # if not razi_module.is_user_logged_in(user[1], user[0]):
                razi_module.log_in_user(user[1], user[0])

                time.sleep(DB.IBSNG_SLEEP_TIME)

            # razi_module.log_out_user(user[1], user[0])

    ibsng_module.close_driver()
    razi_module.close_driver()
