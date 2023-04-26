from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class YourNamePage(BasePage):
    URL = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'

    def __init__(self, driver):
        super().__init__(driver, self.URL)
        self.your_name_text = "label"
        self.select_name = "select[id='userSelect']"
        self.select_name_h = "option[value='2']"
        self.login_button = "button[class$='btn-default']"

    def get_element_text_your_name(self):
        return self.get_text(self.your_name_text)

    def select_your_name(self):
        """Выбрать имя пользователя из выпадающего списка"""
        self.click_element(self.select_name)
        self.wait_for_element(self.select_name_h)

    def get_element_text(self):
        return self.get_text(self.select_name_h)

    def click_login_button(self):
        self.click_button(self.login_button)