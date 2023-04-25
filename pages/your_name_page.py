from pages.base_page import BasePage


class YourNamePage(BasePage):
    URL = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

    def __init__(self, driver):
        super().__init__(driver, self.URL)
        self.your_name_text = "label"

    def get_element_text_your_name(self):
        return self.get_text(self.your_name_text)

