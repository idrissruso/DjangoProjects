from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def home(request):
    if request.method == "POST":
        try:
            user = User.objects.get(user_name=request.post("username"))
        except :
            return HttpResponse("<h1>Not Found</h1>")
    return render(request, "login.html")


def welcome(request):
    return render(request, "index.html")
