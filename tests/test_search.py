from pages.search_page import SearchPage


def test_page_title(driver):
    search_page = SearchPage(driver)
    search_page.open()
    assert "Google" in driver.title