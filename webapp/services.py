from requests import *
from .serializers import RepoSerializer


def get_repos():
    url = 'https://api.github.com/users/githubtraining/repos'
    params = {}
    response = get(url, params=params)
    serializer = RepoSerializer(data=response.json(), many=True)
    serializer.is_valid()
    repos = serializer.validated_data

    return {'repos': repos}
