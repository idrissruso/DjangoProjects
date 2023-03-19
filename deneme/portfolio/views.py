from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def home(request):
    return render(request, "index.html")


def login(request):
    if request.method == "POST":
        data = request.POST
        user = auth.authenticate(username=data["email"], password=data["password"])
        print(user)
        if user is not None:
            auth.login(request=request, user=user)
            print("1")
            return redirect("/")
        else:
            messages.info(request, "İnvalid Credentials")
            print("2")
            return redirect("login")
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        data = request.POST
        if data["password"] == data["Confirm Password"]:
            if User.objects.filter(email=data["email"]).exists():
                messages.info(request, "Email already in use")
                return redirect('register')
            if User.objects.filter(username=data["username"]).exists():
                messages.info(request, "User Name already in use")
                return redirect('register')
            else:
                new_user = User.objects.create_user(username=data["username"], email=data["email"],
                                                    password=data["password"])
                new_user.save()
                return redirect("login")
        else:
            messages.info(request, "Password not matched")
            return redirect('register')

    return render(request, "register.html")
