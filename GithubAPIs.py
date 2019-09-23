import requests
import json
import unittest

def gitData(userID):
    commitCount = 0
    getRepo = requests.get(f"https://api.github.com/users/{userID}/repos") 
    repoData = getRepo.json() #convert to JSON obj
    for entry in repoData:
        name = entry['name']

        getCommits = requests.get(f"https://api.github.com/repos/{userID}/{name}/commits")
        commitData = getCommits.json()
        for entry in commitData:
            if entry["commit"]:
                commitCount += 1
        # print(name, commitCount)
        return(f"Repo: {name} | Number of commits: {commitCount}")
        #store data in an array or dict


class TestGitData(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def test_gitData(self):
        self.assertTrue(len(gitData("ruthylevi")) > 0)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()