from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def home(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def welcome(request):
    return HttpResponse("welcome")
