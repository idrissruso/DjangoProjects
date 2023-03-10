from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request, "index.html", {"name": ["h", "j", "f", "h", "w", "q", "q", "a"]})


def welcome(request):
    return render(request, "index.html")
