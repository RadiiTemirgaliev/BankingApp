from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from logs.logger import logger
from time import sleep

# create a class for the page
class AccountsPage(BasePage):

    # create a method that performs actions on the page
    def select_account(self, account_number):
        # find and click the dropdown
        self.driver.find_element(By.CSS_SELECTOR, "[formcontrolname='accountId']").click()
        sleep(5)

        # find the account number element
        self.driver.find_element(By.XPATH, f"//span[text()='{account_number}']").click()
        sleep(5)