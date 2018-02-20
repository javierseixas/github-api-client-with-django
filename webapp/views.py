from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>HEY!</h2>")

def list(request):
    return render(request, 'webapp/home.html')
