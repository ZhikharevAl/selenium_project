from pages.SeleniumPage import SeleniumPage


def test_example(driver):
    page = SeleniumPage(driver)
    page.open()

    # Locate the child text element within the svg element
    el = page.find_svg_element("1")

    # Print the text of the child element
    print(el.text)

    # Check if the text matches the expected value
    assert "Selenium" in el.text
