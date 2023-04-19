import json
import subprocess
import os
from datetime import datetime

import requests

USERNAME = '0xshimon'
REPO_TO_COMMIT = 'SoNotMalicious'
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_GIT_DIR = 'SET REPO GIT DIR'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
GITHUB_ACCESS_TOKEN = os.environ("GITHUB_ACCESS_TOKEN")


def get_user_repos(fake_committer):
    url = f'https://api.github.com/users/{fake_committer}/repos'
    response = requests.get(url, headers={'User-Agent': USER_AGENT}, auth=(USERNAME, GITHUB_ACCESS_TOKEN))
    return response.json()


def get_commit_by_repo(repo, fake_committer):
    url = f'https://api.github.com/repos/{fake_committer}/{repo}/commits'
    response = requests.get(url, headers={'User-Agent': USER_AGENT}, auth=(USERNAME, GITHUB_ACCESS_TOKEN), params={'author': fake_committer})
    return response.json()


def get_committer_creds(repo_name, fake_committer):
    if not repo_name:
        return False, False
    commits = get_commit_by_repo(repo_name, fake_committer)
    for commit in commits:
        c = (commit.get('commit'))
        cc = (commit.get('commit').get('committer'))
        return commit.get('commit', {}).get('committer', {}).get('name'), commit.get('commit', {}).get('committer', {}).get('email')
    return False, False


def fake_commit(username, email, message='intent2022'):
    print("faking commit")
    os.chdir(REPO_GIT_DIR)
    subprocess.call(['git', 'config', '--global', 'user.name', username])
    subprocess.call(['git', 'config', '--global', 'user.email', email])
    subprocess.call(['touch', "YO.txt"])
    with open('intent2022.txt', 'w+') as f:
        f.write(f'this message was written at {datetime.now()}\n by {username} <{email}> at intent 2022 convention')
    subprocess.call(['git', 'add', '.'])
    subprocess.call(['git', 'commit', '-m', message])
    subprocess.call(['git', 'push', 'origin', 'master'])
    os.chdir(SCRIPT_DIR)


def main(fake_committer, message='boaz'):
    repos = get_user_repos(fake_committer)
    print(repos)
    for repo in repos:
        repo_name = repo.get('name')
        username, email = get_committer_creds(repo_name, fake_committer)
        if not username or not email:
            continue
        fake_commit(username, email, message)
        break

i = 0
while i < 1000:
    main('0xshimon')
    i += 1
