import pytest
from selenium import webdriver
from src.utils.config_reader import load_config


@pytest.fixture(scope="session")
def config():
    return load_config(r"D:\Algoscale wiki automation\config.ini")


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
