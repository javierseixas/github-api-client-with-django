from requests import *
from .serializers import RepoSerializer


def get_repos(orderby='full_name', direction=None):
    url = 'https://api.github.com/users/githubtraining/repos'
    params = _build_params(orderby, direction)
    response = get(url, params=params)
    serializer = RepoSerializer(data=response.json(), many=True)
    serializer.is_valid()
    return serializer.validated_data


def search_repos():
    pass

    # Recover all repos
    # process repos to find per name
    # reponse the found repos


def _build_params(orderby, direction):
    params = {}
    if orderby is not None:
        params['sort'] = orderby
    if direction is not None:
        params['direction'] = direction

    return params