from selenium.webdriver.common.by import By
from time import sleep
from logs.logger import logger

# importing the LoginPage class from LoginPage file
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage

# create test cases
def test_user_logout(driver):
    # create an instance/object of LoginPage class
    login_page = LoginPage(driver)
    # call user_login method of the object
    login_page.user_login()
    # create an instance of HomePage class
    home_page = HomePage(driver)
    home_page.logout()
    # check if Log Out text is displayed
    assert login_page.text_exists('Login')


def test_user_allowed_menus(driver):
    # create an instance/object of LoginPage class
    login_page = LoginPage(driver)
    # call user_login method of the object
    login_page.user_login()
    # create an instance of HomePage class
    home_page = HomePage(driver)
    sleep(5)
    expected_user_menus = {'accounts', 'cards', 'transfers', 'reports', 'news', 'my profile'}
    displayed_user_menus = home_page.get_side_menus()
    logger.info(f'Expected {expected_user_menus}')
    logger.info(f'Displayed {displayed_user_menus}')
    diff = expected_user_menus ^ displayed_user_menus
    assert len(diff) == 0
    

def test_admin_allowed_menus(driver):
    # create an instance/object of LoginPage class
    login_page = LoginPage(driver)
    # call user_login method of the object
    login_page.admin_login()
    # create an instance of HomePage class
    home_page = HomePage(driver)
    expected_admin_menus = {'accounts', 'messages', 'transfers', 'reports', 'news', 'profiles', 'requests', 'settings', 'system log'}
    displayed_admin_menus = home_page.get_side_menus()
    logger.info(f'Expected {expected_admin_menus}')
    logger.info(f'Displayed {displayed_admin_menus}')
    diff = expected_admin_menus ^ displayed_admin_menus
    assert len(diff) == 0