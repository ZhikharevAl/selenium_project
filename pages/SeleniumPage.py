from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SeleniumPage(BasePage):
    URL = 'https://selenium.dev/'

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def find_svg_element(self, id):
        selector = f"svg[id$='{id}']"
        return self.element_is_visible((By.CSS_SELECTOR, selector))
