from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        return driver
    elif browser == "edge":  # pytest
        driver = webdriver.Edge()
        return driver
    elif browser == "firefox":
        driver = webdriver.Firefox()
        return driver

    else:
        driver = webdriver.Chrome()
        return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# ##### pytest HTML reports ###################
# it hooks for adding environment info to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'customer'
    config._metadata['Tester'] = 'Pranit'


# @pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugin", None)
