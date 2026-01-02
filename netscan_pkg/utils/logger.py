import logging
import sys

LOGGER_NAME = "netscan"
logger = logging.getLogger(LOGGER_NAME)


def setup_logger():
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s"
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


def set_verbose(enabled: bool):
    if enabled:
        logger.setLevel(logging.DEBUG)


def debug(message: str):
    logger.debug(message)


def info(message: str):
    logger.info(message)


def warn(message: str):
    logger.warning(message)


def error(message: str):
    logger.error(message)


setup_logger()
