from django.test import TestCase
from webapp.services import Searcher, RepoMapper, Cacher, GithubApiClient
from .models import Repo
from unittest.mock import Mock, patch


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
        self.mapperMock = Mock()
        mocked_repos = [
            Repo('test_repo_1', '2006-10-25 14:30:59.000200', '2006-10-25 14:30:59.000200'),
            Repo('test_repo_2', '2006-10-25 14:30:59.000200', '2006-10-25 14:30:59.000200'),
            Repo('test_repo_3', '2006-10-25 14:30:59.000200', '2006-10-25 14:30:59.000200'),
        ]
        self.mapperMock.convert_from_object_to_model = Mock(side_effect=mocked_repos)
        self.cacher = Cacher(self.mapperMock)

    def test_should_delete_caches_if_api_returns_repos_and_save_repos(self):
        repos = [
            {'name': 'test_repo_1', 'created_at': '20180224T184221Z', 'pushed_at': '20180224T184221Z'},
            {'name': 'test_repo_2', 'created_at': '20180224T184221Z', 'pushed_at': '20180224T184221Z'},
            {'name': 'test_repo_3', 'created_at': '20180224T184221Z', 'pushed_at': '20180224T184221Z'},
        ]

        with patch.object(self.cacher, '_remove_old_cached_elements',
                          wraps=self.cacher._remove_old_cached_elements) as spy:
            self.cacher.record_repos_in_cache(repos)

            self.assertEqual(spy.call_count, 1)

        self.mapperMock.has_calls(3, True)

    def test_should_not_delete_cache_if_no_repos_come_from_the_api(self):
        repos = []

        with patch.object(self.cacher, '_remove_old_cached_elements',
                          wraps=self.cacher._remove_old_cached_elements) as spy:
            self.cacher.record_repos_in_cache(repos)

            self.assertEqual(spy.call_count, 0)


# class GithubApiClientTestCase(TestCase):
#
#     def setUp(self):
#         self.client = GithubApiClient()
#
#     @patch('webapp.services.requests')
#     def test_should_call_github_api(self, mock_requests):
#
#         self.client.get_repos("whatever")
#
#         self.assertTrue(mock_requests.get.called, "Fail doing get request")
#
#         with patch.object(self.client, '_persist_last_visit',
#                           wraps=self.client._persist_last_visit) as spy:
#             self.assertEqual(spy.call_count, 1)

    # @patch('webapp.services.requests')
    # def test_should_call_github_api(self, mock_requests):
    #
    #     self.client.search_repos("whatever")
    #
    #     self.assertTrue(mock_requests.get.called, "Fail doing get request")
    #
    #     with patch.object(self.client, '_persist_last_visit',
    #                       wraps=self.client._persist_last_visit) as spy:
    #         self.assertEqual(spy.call_count, 1)
