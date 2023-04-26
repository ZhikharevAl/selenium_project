import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.account_page import AccountPage
from pages.your_name_page import YourNamePage


def test_your_name(driver):
    page_your_name = YourNamePage(driver)
    page_your_name.open()

    page_your_name.select_your_name()
    your_name_text = page_your_name.get_element_text()

    assert "Harry Potter" in your_name_text, "The 'Harry Potter' text was not found on the page."
    page_your_name.click_login_button()
    page_account = AccountPage(driver)
    page_account_text = page_account.get_element_text()
    
    assert "Harry Potter" in page_account_text, "The 'Harry Potter' text was not found on the page."


