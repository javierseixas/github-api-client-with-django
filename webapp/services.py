from requests import *
from .serializers import RepoSerializer


class GithubApiClient(object):

    url = 'https://api.github.com/users/githubtraining/repos'

    def get_repos(self, orderby='full_name', direction=None):
        params = self._build_params(orderby, direction)
        response = get(self.url, params=params)
        serializer = RepoSerializer(data=response.json(), many=True)
        serializer.is_valid()
        return serializer.validated_data

    def search_repos(self, term):
        response = get(self.url)
        serializer = RepoSerializer(data=response.json(), many=True)
        serializer.is_valid()
        repos = serializer.validated_data

        matched_repos = Searcher().search(repos, term)
        return matched_repos

    def _build_params(self, orderby, direction):
        params = {}
        if orderby is not None:
            params['sort'] = orderby
        if direction is not None:
            params['direction'] = direction

        return params


class Searcher(object):

    def search(self, repos, term):
        return list(filter(lambda repo: term in repo['name'], repos))
