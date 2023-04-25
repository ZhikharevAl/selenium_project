from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SeleniumPage(BasePage):
    URL = 'https://selenium.dev/'

    def __init__(self, driver):
        super().__init__(driver, self.URL)
        self.title_text = "svg[id$='1']"

    def get_title_text(self):
        return self.get_text(self.title_text)


