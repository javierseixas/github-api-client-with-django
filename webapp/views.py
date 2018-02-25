from django.shortcuts import render
from django.views.generic import View
from .services import GithubApiClient, Cacher, RepoMapper
from .forms import SearchRepoForm
from .models import Repo


class ReposView(View):
    template_name = 'webapp/repos.html'

    def get(self, request):

        try:
            search_form = SearchRepoForm()
            orderby = request.GET.get('orderby', 'name')
            repos = GithubApiClient().get_repos(orderby=orderby)

            Cacher().record_repos_in_cache(repos)
        except:
            repos = list(map(lambda repo: RepoMapper().convert_from_model_to_object(repo), Repo.objects.all()))

        return render(request, self.template_name, {'repos': repos, 'search_form': search_form})


class SearchView(View):
    template_name = 'webapp/search_results.html'

    def get(self, request):
        search_form = SearchRepoForm()
        term = request.GET.get('term', '')
        repos = GithubApiClient().search_repos(term)

        return render(request, self.template_name, {
            'repos': repos,
            'search_form': search_form,
            'searched_term': term,
            'flag_back_to_list': True,
        })
