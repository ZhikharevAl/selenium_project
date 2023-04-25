from selenium.webdriver.common.by import By

from pages.base_page import BasePage


def test_example(driver):
    page = BasePage(driver, ' http://selenium.dev/')
    page.open()

    # Locate the child text element within the svg element
    el = page.element_is_visible((By.CSS_SELECTOR, "svg[id$='1']"))

    # Print the text of the child element
    print(el.text)

    # Check if the text matches the expected value
    assert "Selenium" in el.text
