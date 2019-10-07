import unittest
import json
from unittest import mock
import GithubAPIs

class TestGithubAPI(unittest.TestCase):

    '''
    This class mock out all of the service calls 
    in GithubAPIs.py using the python mock module
    '''

    @mock.patch('GithubAPIs.get_repos', return_value =  [{'name': 'Mock'}, {'name': 'Triangle567'}])
    @mock.patch('GithubAPIs.get_commits', return_value = 2)    

    def test_commitCount(self, mockA, mockB):
        self.assertEqual(GithubAPIs.commit_count('Mock')['Mock'], 2)
        self.assertIn('Mock', GithubAPIs.commit_count('Mock'))

    @mock.patch('GithubAPIs.requests.get')
    def test_get_repos(self, mockedRequest):
        mockedRequest.return_value.json.return_value = [{'name': 'ruthylevi.github.io'},{'name': 'Mock'}]
        self.assertIn({'name': 'ruthylevi.github.io'}, GithubAPIs.get_repos('Mock'))

    @mock.patch('GithubAPIs.requests.get')
    def test_get_commits(self, mockedRequest):
        mockedRequest.return_value.json.return_value = [{'commit': 'first_commit'},{'commit': 'second_commit'}]
        commits = GithubAPIs.get_commits('Mock', 'Mock_Repo')
        self.assertEqual(commits, 2)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()