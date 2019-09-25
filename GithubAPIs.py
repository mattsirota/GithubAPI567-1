import requests
import json
import unittest

def gitData(userID):
    commitCount = 0
    dict = {}
    getRepo = requests.get(f"https://api.github.com/users/{userID}/repos") 
    repoData = getRepo.json() #convert to JSON obj
    for entry in repoData:
        name = entry['name']

        getCommits = requests.get(f"https://api.github.com/repos/{userID}/{name}/commits")
        commitData = getCommits.json()
        for entry in commitData:
            if entry["commit"]:
                commitCount += 1
        dict[name] = commitCount
    return dict

class TestGitData(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def test_gitData(self):
        self.assertTrue(len(gitData("ruthylevi")) > 0)

    def test_repo(self):
        self.assertEquals(gitData('Asupkay')['Raffler'], 465)
         
    def test_commitCount(self):
        self.assertEquals(gitData('Zildj')['CXIA'], 9)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()