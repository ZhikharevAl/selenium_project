from pages.base_page import BasePage


class AccountPage(BasePage):
    URL = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'

    def __init__(self, driver):
        super().__init__(driver, self.URL)
        self.welcome_text = "span[class^='fontBig']"

    def get_element_text(self):
        return self.get_text(self.welcome_text)