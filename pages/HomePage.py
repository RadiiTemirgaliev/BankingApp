from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from logs.logger import logger

# create a class for the page
class HomePage(BasePage):

    logout_button = By.CSS_SELECTOR, 'div.controls__logout > span'


    # create a method that performs actions on the page
    def logout(self):
        self.driver.find_element(*self.logout_button).click()
        logger.info('Clicked on Logout Button')
    

    def get_side_menus(self):
        side_menus = self.driver.find_elements(By.CSS_SELECTOR, 'label.aside__label')
        return {menu.text.lower() for menu in side_menus}