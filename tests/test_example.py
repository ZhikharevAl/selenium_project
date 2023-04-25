from pages.SeleniumPage import SeleniumPage


def test_example(driver):
    page = SeleniumPage(driver)
    page.open()

    # Locate the child text element within the svg element
    el = page.get_title_text()

    # Check if the text matches the expected value
    assert "Selenium" in el
