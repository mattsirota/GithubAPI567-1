import requests
import json

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
    print(dict)

if __name__ == '__main__':
    gitData('ruthylevi')