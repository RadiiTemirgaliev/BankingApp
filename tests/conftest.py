import pytest
from selenium import webdriver
from datetime import datetime
import os
from logs.logger import logger
from configs import config

@pytest.fixture()
def driver():
    # steps to run before each test case, setup
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    logger.info(f'########## Test Case: {test_name} ##########')
    driver = webdriver.Firefox()
    logger.info('Opened Firefox Browser')
    driver.get(config.URL)
    logger.info('Launched the application')
    driver.implicitly_wait(config.TIMEOUT)
    driver.maximize_window()

    # pass/give the driver to the test case
    yield driver

    # steps to run after each test case, teardown
    # driver.save_screenshot(r'.\evidence\screenshot.png')
    
    timestamp = datetime.now().strftime('%m%d%y_%H%M%S')
    driver.save_screenshot(fr".\evidence\{test_name}_{timestamp}.png")
    driver.quit()
    logger.info('Closed the browser')


@pytest.fixture
def setup():
    driver = webdriver.Firefox()
    driver.get('https://demo.ebanq.com/log-in')
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    
    