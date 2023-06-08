from pages.BasePage import BasePage
from logs.logger import logger
from configs import config


from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    # class attribute
    email_field = By.CSS_SELECTOR, '[type="email"]'
    password_field = By.CSS_SELECTOR, '[type="password"]'
    submit_button = By.CSS_SELECTOR, '[type="submit"]'


    def login(self, username, password):
        self.driver.find_element(*self.email_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        logger.info(f'User entered username: {username} and password: {password}')
        self.driver.find_element(*self.submit_button).click()
        logger.info('User clicked the Log In Button')


    def user_login(self):
        self.login(config.USER, config.USER_PASSWORD)

    
    def admin_login(self):
        self.login(config.ADMIN, config.ADMIN_PASSWORD)

    
    def invalid_user_login(self, username, password):
        self.driver.find_element(*self.email_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.submit_button).click()
        

