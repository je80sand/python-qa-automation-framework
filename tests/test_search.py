def test_intentional_failure(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    assert "Google" in driver.title