import time

from pages.account_page import AccountPage
from pages.your_name_page import YourNamePage


def test_button_transactions(login, driver):
    page_account = AccountPage(driver)
    page_account.open()
    page_account.click_button_transactions()

    data_time_text = page_account.text_date_time()
    assert "Date-Time" in data_time_text, "The 'Date-Time' button was not found on the page."


def test_button_deposit(login, driver):
    page_account = AccountPage(driver)
    page_account.open()
    page_account.click_button_deposit()
    
    amount_to_be_deposited_text = page_account.text_amount_to_be_deposited()
    assert "Amount to be Deposited" in amount_to_be_deposited_text, "The 'Amount to be Deposited' text was not found " \
                                                                    "on the page."


def test_button_withdrawl(login, driver):
    page_account = AccountPage(driver)
    page_account.open()
    page_account.click_button_withdrawl()

    amount_to_be_withdrawn_text = page_account.text_amount_to_be_withdrawn()
    assert "Amount to be Withdrawn" in amount_to_be_withdrawn_text, "The 'Amount to be Withdrawn' text was not found " \
                                                                    "on the page."
