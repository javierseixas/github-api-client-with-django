from django.shortcuts import render
from django.http import HttpResponse
from . import services


def index(request):
    return HttpResponse("<h2>HEY!</h2>")


def list(request):
    return render(request, 'webapp/home.html')


def with_api(request):
    repos = services.get_repos()
    return render(request, 'webapp/repos.html', repos)
