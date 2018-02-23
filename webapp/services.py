from requests import *
from .serializers import RepoSerializer
from .models import Stats, Repo
from datetime import datetime


class GithubApiClient(object):

    url = 'https://api.github.com/users/githubtraining/repos'

    def get_repos(self, orderby='full_name', direction=None):
        params = self._build_params(orderby, direction)
        response = get(self.url, params=params)
        serializer = RepoSerializer(data=response.json(), many=True)
        serializer.is_valid()

        self._persist_last_visit()

        return serializer.validated_data

    def search_repos(self, term):
        response = get(self.url)
        serializer = RepoSerializer(data=response.json(), many=True)
        serializer.is_valid()
        repos = serializer.validated_data

        self._persist_last_visit()

        matched_repos = Searcher().search(repos, term)
        return matched_repos

    def _build_params(self, orderby, direction):
        params = {}
        if orderby is not None:
            params['sort'] = orderby
        if direction is not None:
            params['direction'] = direction

        return params

    def _persist_last_visit(self):
        record_visit = Stats(name='last_api_request', value=datetime.now())
        try:
            record_visit.save(force_update=True)
        except:
            record_visit.save(force_insert=True)


class Searcher(object):

    def search(self, repos, term):
        return list(filter(lambda repo: term in repo['name'], repos))


class Cacher(object):
    elements_count = 10

    def record_repos_in_cache(self, repos):
        self._remove_old_cached_elements()

        for repo in repos[:self.elements_count]:
            repo_model = RepoMapper().convert_from_object_to_model(repo)
            repo_model.save(force_insert=True)

    def _remove_old_cached_elements(self):
        Repo.objects.all().delete()


class RepoMapper(object):
    def convert_from_object_to_model(self, repo):
        return Repo(repo['name'], repo['created_at'], repo['pushed_at'])