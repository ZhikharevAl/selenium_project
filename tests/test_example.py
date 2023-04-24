from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-insecure-localhost')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


def test_example():
    driver.get('http://selenium.dev/')

    # Locate the child text element within the svg element
    el = driver.find_element(By.CSS_SELECTOR, "svg[id$='1']")

    # Print the text of the child element
    print(el.text)

    # Check if the text matches the expected value
    assert "Selenium" in el.text

    driver.quit()
