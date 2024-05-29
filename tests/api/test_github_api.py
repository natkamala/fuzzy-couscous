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

    @pytest.mark.api
def test_get_emojis(github_api):
    """Тестує отримання списку Emoji."""
    result = github_api.get_emojis()
    assert 'octocat' in result  

@pytest.mark.api
def test_list_commits(github_api):
    """Тестує отримання комітів репозиторію."""
    owner = "octocat"
    repo = "Hello-World"
    result = github_api.list_commits(owner, repo)
    assert isinstance(result, list)
    assert 'commit' in result[0]  

@pytest.mark.api
def test_commit_pagination(github_api):
    """Тестує пагінацію комітів."""
    owner = "octocat"
    repo = "Hello-World"
    result = github_api.list_commits(owner, repo)
    assert len(result) <= 30  

@pytest.mark.api
def test_no_commits_for_empty_repo(github_api):
    """Тестує відсутність комітів у порожньому репозиторії."""
    owner = "octocat"
    repo = "empty-repo"
    result = github_api.list_commits(owner, repo)
    assert result == []  
    