import pytest
from selenium import webdriver
import logging


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.close()


@pytest.fixture(scope="session")
def logger():
    DATEFMT = '%d-%m-%Y %H:%M:%S'
    FORMAT = "%(asctime)s [%(levelname)s] %(funcName)-15s: %(message)s"
    logger = logging.getLogger("common_log")
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(f"logs.log", mode='a', encoding="UTF-8")
    formatter = logging.Formatter(FORMAT, DATEFMT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info("Begin session")
    yield logger
    logger.info("End session")
