from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait as wait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def get_text(self, selector):
        element = wait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
        )
        return element.text

    def get_text_xpath(self, selector):
        element = wait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, selector))
        )
        return element.text

    def click_button(self, selector):
        button = wait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        )
        button.click()

    def click_element(self, selector):
        element = wait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        element.click()

    def wait_for_element(self, selector):
        element = wait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        element.click()


