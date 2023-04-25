from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

    def __init__(self, driver):
        super().__init__(driver, self.URL)
        self.xyz_bank_text = "strong[class='mainHeading']"
        self.customer_login_button = "button[ng-click='customer()']"

    def get_element_text(self):
        return self.get_text(self.xyz_bank_text)

    def click_customer_login_button(self):
        return self.click_button(self.customer_login_button)
