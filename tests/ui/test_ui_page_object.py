import pytest
from modules.ui.page_object.sign_in_page import SignInPage

@pytest.mark.ui
def test_invalid_sign_in():
    sign_in_page = SignInPage()
    try:
        sign_in_page.sign_in('invalid_user', 'invalid_password')
        assert sign_in_page.is_title_correct('Expected Title'), "Title does not match expected title."
    finally:
        sign_in_page.close()
        
