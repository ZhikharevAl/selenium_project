import time

from pages.login_page import LoginPage
from pages.your_name_page import YourNamePage


def test_title_xyz_bank_page(driver):
    page = LoginPage(driver)
    page.open()

    xyz_bank_text = page.get_element_text()

    assert "XYZ Bank" in xyz_bank_text, "The 'XYZ Bank' text was not found on the page."


def test_customer_login_button(driver):
    page = LoginPage(driver)
    page.open()
    page.click_customer_login_button()
    xyz_bank_text = page.get_element_text()
    page_your_name = YourNamePage(driver)
    your_name_text = page_your_name.get_element_text_your_name()
    assert "XYZ Bank" in xyz_bank_text, "The 'XYZ Bank' text was not found on the page."
    assert "Your Name" in your_name_text, "The 'Your Name' text was not found on the page."
