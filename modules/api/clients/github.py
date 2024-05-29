import requests

class GitHub:
    def __init__(self):
        self.base_url = "https://api.github.com/users/"

    def get_user(self, username):
        url = f"{self.base_url}{username}"
        response = requests.get(url)
        return response.json()

    def search_repo(self, name):
        url = "https://api.github.com/search/repositories"
        response = requests.get(url, params={'q': name})
        return response.json()