from time import sleep
import pytest
from logs.logger import logger
from pages.AccountInformation import AccountInformation
from pages.LoginPage import LoginPage
from pages.AccountsPage import AccountsPage


account_numbers = ['EBQ11113487654', 'EBQ11223487456', 'EBQ11223387654', 'EBQ38495629375', '511264340']

expected_values = {
    'EBQ11113487654': {
        'holder_name': 'John Doe',
        'currency': 'EUR',
        'status': 'Active',
        'account_type': 'Checking'
    },
    'EBQ11223487456': {
        'holder_name': 'John Doe',
        'currency': 'EUR',
        'status': 'Active',
        'account_type': 'Savings'
    },
    'EBQ11223387654': {
        'holder_name': 'John Doe',
        'currency': 'EUR',
        'status': 'Active',
        'account_type': 'Savings'
    },
    'EBQ38495629375': {
        'holder_name': 'John Doe',
        'currency': 'USD',
        'status': 'Active',
        'account_type': 'Checking'
    },
    '511264340': {
        'holder_name': 'John Doe',
        'currency': 'BTC',
        'status': 'Active',
        'account_type': 'BTC Wallet'
    }
}


@pytest.mark.parametrize("account_number", account_numbers)
def test_selected_account_information(driver, account_number):
    login_page = LoginPage(driver)
    logger.info('User launched the browser')
    login_page.user_login()
    accounts_page = AccountsPage(driver)
    logger.info('User clicked to accounts dropdown menu')
    accounts_page.select_account(account_number)
    logger.info(f'User selected account: {account_number}')

    dropdown_page = AccountInformation(driver)  # Create an instance of AccountInformation

    holder_name = dropdown_page.get_holder_name()
    current_balance = dropdown_page.get_current_balance()
    available_balance = dropdown_page.get_available_balance()
    currency = dropdown_page.get_currency()
    status = dropdown_page.get_status()
    account_type = dropdown_page.get_account_type()

    expected_values_for_account = expected_values[account_number]

    assert holder_name[-8:] == expected_values_for_account['holder_name']
    assert currency == expected_values_for_account['currency']
    assert status == expected_values_for_account['status']
    assert account_type == expected_values_for_account['account_type']
    assert current_balance is not None and current_balance != ""
    assert available_balance is not None and available_balance != ""