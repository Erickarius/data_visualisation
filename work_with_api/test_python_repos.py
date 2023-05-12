import unittest
import requests

class TestPythonRepos(unittest.TestCase):
    def test_status_code(self):
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        headers = {'Accept': 'application/vnd.github.v3+json'}
        r = requests.get(url, headers=headers)
        self.assertEqual(r.status_code, 200)

    def test_number_of_repos(self):
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        headers = {'Accept': 'application/vnd.github.v3+json'}
        r = requests.get(url, headers=headers)
        response_dict = r.json()
        repo_dicts = response_dict['items']
        self.assertGreater(len(repo_dicts), 0)

if __name__ == '__main__':
    unittest.main()
