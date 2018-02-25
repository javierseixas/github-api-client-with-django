from django.test import TestCase
from webapp.services import Searcher


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
