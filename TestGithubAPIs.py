import json
import unittest
from unittest import mock
from GithubAPI import gitData

class TestGitData(unittest.TestCase):
    '''
    This class mock out all of the service calls 
    in GithubAPI.py using the python mock module
    '''
    @mock.patch('GithubAPI.requests.get')
    def test_gitData(self, mockedRequest):
        mockedRequest.return_value.json.return_value = [{'name': 'Mock'}, {'name': 'GithubAPI567'}]
        self.assertTrue(len(gitData("Mock")) > 0)

    @mock.patch('GithubAPI.requests.get')
    def test_repo(self, mockedRequest):
        mockedRequest.return_value.json = [{'name': 'Triangle567'},{'name': 'Mock'}]
        self.assertEquals(gitData('Mock')['Mock'], 2)
    
    @mock.patch('GithubAPI.requests.get')
    def test_commitCount(self, mockedRequest):
        mockedRequest.return_value.json = [{'name': 'GitHubApi567'},{'name': 'Triangle567'},{'name': 'Mock'}]
        self.assertEquals(gitData('Mock')['Mock'], 3)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()