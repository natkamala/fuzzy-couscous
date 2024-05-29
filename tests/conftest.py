import pytest
from modules.api.clients.github import GitHub

@pytest.fixture
def github_api():
    return GitHub()
