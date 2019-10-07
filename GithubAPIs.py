import requests
import json

def commit_count(userID):
    repos = get_repos(userID)
    dict = {}
    for entry in repos:
        repoName = entry["name"]
        dict[repoName] = get_commits(userID, repoName)
    return dict
        
def get_repos(userID):
    getRepo = requests.get(f"https://api.github.com/users/{userID}/repos").json()
    return getRepo

def get_commits(userID, repoName):
    commitURL = requests.get(f"https://api.github.com/repos/{userID}/{repoName}/commits").json()
    return len(commitURL)

# if __name__ == "__main__":
#     commit_count('ruthylevi')