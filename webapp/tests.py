from django.test import TestCase
from webapp.services import Searcher, RepoMapper, Cacher
from .models import Repo
from mock import Mock, patch


class SearcherTestCase(TestCase):

    def setUp(self):
        self.searcher = Searcher()

    def test_should_return_objects_with_searched_term(self):
        repos = [
            {'name': 'bar'},
            {'name': 'foo'},
        ]
        results = self.searcher.search(repos, term='foo')
        expected = [{'name': 'foo'}]

        self.assertEqual(expected, results)

    def test_should_return_objects_with_partial_searched_term(self):
        repos = [
            {'name': 'bar'},
            {'name': 'foo'},
        ]
        results = self.searcher.search(repos, term='ba')
        expected = [{'name': 'bar'}]

        self.assertEqual(expected, results)

    def test_should_return_empty_if_no_matching(self):
        repos = [
            {'name': 'bar'},
            {'name': 'foo'},
        ]
        results = self.searcher.search(repos, term='var')
        expected = []

        self.assertEqual(expected, results)


class RepoMapperTestCase(TestCase):

    def setUp(self):
        self.mapper = RepoMapper()

    def test_should_convert_from_object_to_model(self):
        repo = {'name': 'test_repo', 'created_at': '20180224T184221Z', 'pushed_at': '20180224T184221Z'}
        result = self.mapper.convert_from_object_to_model(repo)
        expected = Repo('test_repo', '20180224T184221Z', '20180224T184221Z')

        self.assertEqual(expected, result)

    def test_should_convert_from_model_to_object(self):
        repo = Repo('test_repo', '20180224T184221Z', '20180224T184221Z')
        result = self.mapper.convert_from_model_to_object(repo)
        expected = {'name': 'test_repo', 'created_at': '20180224T184221Z', 'pushed_at': '20180224T184221Z'}

        self.assertEqual(expected, result)


class CacherTestCase(TestCase):

    def setUp(self):
        mapperMock = mock()
        self.cacher = Cacher()

    def test_should_delete_and_record_repos(self):

        repos = [
            {'name': 'test_repo_1', 'created_at': '20180224T184221Z', 'pushed_at': '20180224T184221Z'},
            {'name': 'test_repo_2', 'created_at': '20180224T184221Z', 'pushed_at': '20180224T184221Z'},
            {'name': 'test_repo_3', 'created_at': '20180224T184221Z', 'pushed_at': '20180224T184221Z'},
        ]

        self.cacher.record_repos_in_cache(repos)

        self.assert()
