from django.conf.urls import url
from django.views.generic import ListView, DetailView
from webapp.models import Repo


urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Repo.objects.all().order_by("-name")[:25], template_name='webapp/home.html'))
]
