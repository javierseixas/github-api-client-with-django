from django.conf.urls import url
from django.views.generic import ListView
from .models import Repo
from .views import ReposView, SearchView


urlpatterns = [
    url(r'^repos/$', ReposView.as_view()),
    url(r'^repos/search/', SearchView.as_view()),
]
