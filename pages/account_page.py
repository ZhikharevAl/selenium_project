from pages.base_page import BasePage


class AccountPage(BasePage):
    URL = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'

    def __init__(self, driver):
        super().__init__(driver, self.URL)
        self.welcome_text = "span[class^='fontBig']"
        self.button_transactions = "button[ng-class='btnClass1']"
        self.button_deposit = "button[ng-class='btnClass2']"
        self.button_withdrawl = "button[ng-class='btnClass3']"
        self.date_time_text = "a[ng-click^='sortType']"
        self.amount_to_be_deposited = "//*[text() = 'Amount to be Deposited :']"
        self.amount_to_be_withdrawn = "//*[text() = 'Amount to be Withdrawn :']"

    def get_element_text(self):
        return self.get_text(self.welcome_text)

    def click_button_transactions(self):
        self.click_button(self.button_transactions)

    def click_button_deposit(self):
        self.click_button(self.button_deposit)

    def click_button_withdrawl(self):
        self.click_button(self.button_withdrawl)

    def text_date_time(self):
        return self.get_text(self.date_time_text)

    def text_amount_to_be_deposited(self):
        return self.get_text_xpath(self.amount_to_be_deposited)

    def text_amount_to_be_withdrawn(self):
        return self.get_text_xpath(self.amount_to_be_withdrawn)
