from django.shortcuts import render
from django.http import HttpResponse
from . import services


def index(request):
    return HttpResponse("<h2>HEY!</h2>")


def list(request):
    return render(request, 'webapp/home.html')


def with_api(request):
    orderby = request.GET.get('orderby', 'name')
    repos = services.get_repos(orderby=orderby)
    return render(request, 'webapp/repos.html', repos)


def search(request):
    term = request.GET.get('search', 'name')
    repos = services.get_repos(search)
    return render(request, 'webapp/repos.html', repos)
