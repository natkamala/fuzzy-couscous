import pytest

@pytest.mark.api
def test_user_exists(github_api):
    username = "defunkt"
    result = github_api.get_user(username)
    assert result['login'] == username

@pytest.mark.api
def test_user_not_exists(github_api):
    username = "butenkosergii"
    result = github_api.get_user(username)
    assert 'message' in result and result['message'] == "Not Found"

@pytest.mark.api
def test_repo_can_be_found(github_api):
    repo_name = "become-qa-auto"
    result = github_api.search_repo(repo_name)
    assert result['total_count'] == 25

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    repo_name = "sergiibutenko_repo_non_exist"
    result = github_api.search_repo(repo_name)
    assert result['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    repo_name = "s"
    result = github_api.search_repo(repo_name)
    assert result['total_count'] != 0
    