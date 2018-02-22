from requests import *


def get_repos():
    url = 'https://api.github.com/users/githubtraining/repos'
    params = {'per_page': 2}
    print('IM HERE ----------------------')
    r = get(url, params=params)
    repos = r.json()
    repos_list = {'repos':repos}

    print(repos_list)

    return repos_list