from django.conf.urls import url
from django.views.generic import ListView
from .models import Repo
from . import views


urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Repo.objects.all().order_by("-name")[:25], template_name='webapp/home.html')),
    url(r'^repos/', views.with_api),
]
