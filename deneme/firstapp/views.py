from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return HttpResponse("hello wordl")


def welcome(request):
    return render(request, "index.html")
