from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        data = request.POST

        redirect('register')
    return render(request, "register.html")
