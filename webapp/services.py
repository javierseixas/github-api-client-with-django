from requests import *
from .serializers import RepoSerializer


def get_repos(orderby='full_name', direction=None):
    url = 'https://api.github.com/users/githubtraining/repos'
    params = _build_params(orderby, direction)
    response = get(url, params=params)
    serializer = RepoSerializer(data=response.json(), many=True)
    serializer.is_valid()
    return serializer.validated_data

# TODO Refactor duplicated code
def search_repos(term):
    url = 'https://api.github.com/users/githubtraining/repos'
    params = {}
    response = get(url, params=params)
    serializer = RepoSerializer(data=response.json(), many=True)
    serializer.is_valid()
    repos = serializer.validated_data

    filtered_repos = Searcher().search(repos, term)
    return filtered_repos

def _build_params(orderby, direction):
    params = {}
    if orderby is not None:
        params['sort'] = orderby
    if direction is not None:
        params['direction'] = direction

    return params


class Searcher(object):

    def search(self, repos, term):
        return list(filter(lambda repo: term in repo['name'], repos))
