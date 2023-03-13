from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def home(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        data = request.POST
        if data["password"] == data["Confirm Password"]:
            if User.objects.filter(email=data["email"]).exists():
                messages.info(request, "Email already in use")
                redirect('register')
            if User.objects.filter(username=data["username"]).exists():
                messages.info(request, "User Name already in use")
                redirect('register')
            else:
                new_user = User.objects.create_user(username=data["username"], email=data["email"],
                                                    password=data["password"])
                new_user.save()
                redirect('register')
        else:
            messages.info(request, "Password not matched")
            redirect('register')

        redirect('register')
    return render(request, "register.html")
