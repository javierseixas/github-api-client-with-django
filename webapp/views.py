from django.shortcuts import render
from django.views.generic import View
from .services import GithubApiClient
from .forms import SearchRepoForm


class ReposView(View):
    template_name = 'webapp/repos.html'

    def get(self, request):
        search_form = SearchRepoForm()
        orderby = request.GET.get('orderby', 'name')
        repos = GithubApiClient().get_repos(orderby=orderby)

        return render(request, self.template_name, {'repos': repos, 'search_form': search_form})


class SearchView(View):
    template_name = 'webapp/repos.html'

    def get(self, request):
        search_form = SearchRepoForm()
        term = request.GET.get('term', '')
        repos = GithubApiClient().search_repos(term)

        return render(request, self.template_name, {
            'repos': repos,
            'search_form': search_form,
            'searched_term': term
        })
