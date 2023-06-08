
from selenium.webdriver.common.by import By
from configs import config
from time import sleep
from logs.logger import logger

# create a class for the page
class BasePage:

    # create constructor method for page object
    def __init__(self, driver) -> None:
        self.driver = driver
    

    def text_exists(self, text):
        wait = 0
        while wait < config.TIMEOUT:
            if text.lower() not in self.driver.page_source.lower():
                sleep(1)
                wait += 1
                logger.info(f'Waited for {wait} seconds ... ')
            else:
                logger.info(f'Found the {text} on the page. Waited for {wait} seconds ... ')
                return True
        logger.info(f'Text [{text}] was not found on the page. Waited for {wait} seconds ... ')
        return False


