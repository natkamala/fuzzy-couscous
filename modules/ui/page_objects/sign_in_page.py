from .base_page import BasePage

class SignInPage(BasePage):
    def __init__(self):
        super().__init__()

    def sign_in(self, username, password):
        self.driver.find_element_by_id('email').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_id('sign-in-button').click()

    def is_title_correct(self, expected_title):
        return self.driver.title == expected_title
    