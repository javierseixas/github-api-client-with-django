from django.shortcuts import render
from django.http import HttpResponse
from . import services
from .forms import SearchRepoForm


def index(request):
    return HttpResponse("<h2>HEY!</h2>")


def list(request):
    search_form = SearchRepoForm()
    orderby = request.GET.get('orderby', 'name')
    repos = services.get_repos(orderby=orderby)
    return render(request, 'webapp/repos.html', {'repos': repos, 'search_form': search_form})


def search(request):
    term = request.GET.get('search', 'name')
    repos = services.get_repos(search)
    return render(request, 'webapp/repos.html', {'repos': repos})
