import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


from pages.your_name_page import YourNamePage


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-insecure-localhost')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login(driver):
    page_your_name = YourNamePage(driver)
    page_your_name.open()
    page_your_name.select_your_name()
    page_your_name.click_login_button()

