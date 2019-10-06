import unittest
import json
from unittest import mock
import GithubAPIs

class TestGithubAPI(unittest.TestCase):
    '''
    This class mock out all of the service calls 
    in GithubAPI.py using the python mock module
    '''
    @mock.patch('GithubAPI.get_repos', return_value = ['ruthylevi.github.io', 'Mock'])
    @mock.patch('GithubAPI.get_commits', return_value = 2)    
    def test_commitCount(self, mockedRequest):
        self.assertEquals(GithubAPI.commit_count('Mock')['Mock'], 2)

    @mock.patch('GithubAPI.requests.get')
    def test_get_repos(self, mockedRequest):
        mockedRequest.return_value.json = [{'name': 'ruthylevi.github.io'},{'name': 'Mock'}]
        self.assertIn('ruthylevi.github.io', GithubAPI.get_repos('Mock'))
    
    @mock.patch('GithubAPI.requests.get')
    def test_get_commits(self, mockedRequest):
        mockedRequest.return_value.json.return_value = [{'commit': 'first_commit'},{'commit': 'second_commit'}]
        commits = GithubAPI.get_commits('Mock', 'Mock_Repo')
        self.assertEquals(commits, 2)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()