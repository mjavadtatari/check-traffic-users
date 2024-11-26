import logging


def create_logger(path, log_format):
    """
    Create and configuring the logger
    """

    logger = logging.getLogger(__name__)
    logger.setLevel('INFO')

    file_handler = logging.FileHandler(path, mode='w', encoding='utf-8')

    file_format = logging.Formatter(log_format)
    file_handler.setFormatter(file_format)

    logger.addHandler(file_handler)

    return logger
