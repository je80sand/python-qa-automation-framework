import pytest
from pages.login_page import LoginPage
from utils.config_reader import load_test_data


test_data = load_test_data("test_data/test_users.json")


@pytest.mark.parametrize(
    "user_key, expected_text",
    [
        ("valid_user", "You logged into a secure area!"),
        ("invalid_user", "Your username is invalid!")
    ]
)
def test_login_scenarios(driver, user_key, expected_text):
    user = test_data[user_key]

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(user["username"], user["password"])

    message = login_page.get_flash_message()

    assert expected_text in message