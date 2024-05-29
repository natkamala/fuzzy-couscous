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

@pytest.mark.api
def test_handle_http_error(github_api):
    owner = "octocat"
    repo = "nonexistent-repo"
    result = github_api.get_branches(owner, repo)
    assert result.get('message') == "Not Found"
    assert 'documentation_url' in result 

@pytest.mark.api
def test_rate_limit(github_api):
    owner = "octocat"
    repo = "Hello-World"
    for _ in range(1000):  
        github_api.get_branches(owner, repo)
    result = github_api.get_branches(owner, repo)
    assert 'rate limit exceeded' in result.get('message', '').lower()

@pytest.mark.api
def test_caching(github_api):
    owner = "octocat"
    repo = "Hello-World"
    first_response = github_api.get_branches(owner, repo)
    second_response = github_api.get_branches(owner, repo)
    assert first_response == second_response

class GitHub:
    def __init__(self):
        self.base_url = "https://api.github.com/"

    def get_branches(self, owner, repo):
        url = f"{self.base_url}repos/{owner}/{repo}/branches"
        response = requests.get(url)
        return response.json()

    def get_releases(self, owner, repo):
        url = f"{self.base_url}repos/{owner}/{repo}/releases"
        response = requests.get(url)
        return response.json()
    
    import pytest

@pytest.mark.api
def test_get_branches(github_api):
    owner = "octocat"
    repo = "Hello-World"
    result = github_api.get_branches(owner, repo)
    assert isinstance(result, list)
    assert "master" in [branch['name'] for branch in result]

@pytest.mark.api
def test_get_releases(github_api):
    owner = "octocat"
    repo = "Hello-World"
    result = github_api.get_releases(owner, repo)
    assert isinstance(result, list)

@pytest.mark.api
def test_no_releases_for_new_repo(github_api):
    owner = "octocat"
    repo = "new-repo"
    result = github_api.get_releases(owner, repo)
    assert result == []

@pytest.mark.api
def test_branches_in_empty_repo(github_api):
    owner = "octocat"
    repo = "empty-repo"
    result = github_api.get_branches(owner, repo)
    assert result == []













   
