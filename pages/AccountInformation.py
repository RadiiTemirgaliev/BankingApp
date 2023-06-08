from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class AccountInformation(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.holder_name = (By.XPATH, "//span[text()='Hello , John Doe']")
        self.current_balance = (By.XPATH, "//div[text()='Current Balance']/following-sibling::div[1]")
        self.available_balance = (By.XPATH, "//div[text()='Current Balance']/following-sibling::div[2]")
        self.currency = (By.XPATH, "//div[text()='Currency']/following-sibling::div")
        self.status = (By.XPATH, "//div[text()='Status']/following-sibling::div")
        self.account_type = (By.XPATH, "//div[text()='Account type']/following-sibling::div")

    
    def get_holder_name(self):
        return self.driver.find_element(*self.holder_name).text

    def get_current_balance(self):
        return self.driver.find_element(*self.current_balance).text

    def get_available_balance(self):
        return self.driver.find_element(*self.available_balance).text

    def get_currency(self):
        return self.driver.find_element(*self.currency).text

    def get_status(self):
        return self.driver.find_element(*self.status).text

    def get_account_type(self):
        return self.driver.find_element(*self.account_type).text
    