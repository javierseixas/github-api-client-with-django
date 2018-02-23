from django.shortcuts import render
from . import services
from .forms import SearchRepoForm
from django.views.generic import View


class ReposView(View):
    template_name = 'webapp/repos.html'

    def get(self, request):
        search_form = SearchRepoForm()
        orderby = request.GET.get('orderby', 'name')
        repos = services.get_repos(orderby=orderby)

        return render(request, self.template_name, {'repos': repos, 'search_form': search_form})


class SearchView(View):
    template_name = 'webapp/repos.html'

    def get(self, request):
        search_form = SearchRepoForm()
        term = request.GET.get('term', '')
        repos = services.search_repos(term)

        return render(request, self.template_name, {
            'repos': repos,
            'search_form': search_form,
            'searched_term': term
        })
