def test_page_title(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    assert "The Internet" in driver.title