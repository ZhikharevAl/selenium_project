from pages.base_page import BasePage


class AccountPage(BasePage):
    URL = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'

    def __init__(self, driver):
        super().__init__(driver, self.URL)
        self.welcome_text = "span[class^='fontBig']"
        self.button_transactions = "button[ng-class='btnClass1']"
        self.button_deposit = "button[ng-class='btnClass2']"
        self.button_withdrawl = "button[ng-class='btnClass3']"

    def get_element_text(self):
        return self.get_text(self.welcome_text)

    def click_button_transactions(self):
        self.click_button(self.button_transactions)