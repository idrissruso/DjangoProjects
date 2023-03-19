from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    if request.method == "POST":
        data = request.POST
        if data["password"] == data["c_password"]:
            if User.objects.filter(email=data["email"]).exists():
                messages.info(request, "Email already in use")
                return redirect("register")
            elif User.objects.filter(username=data["name"]).exists():
                messages.info(request, "Username already in use")
                return redirect("register")
            else:
                user = User.objects.create_user(username=data["name"], email=data["email"], password=data["password"])
                user.save()
                return redirect("login")
                
        else:
            messages.info(request=request, message="Passwords do not match")
            return redirect("register")
    return render(request, "register.html")



from django.contrib import auth

def login(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(request,username=data["username"], password=data["password"])
        if user :
            auth.login(request=request,user=user)
            return redirect("welcome")
        else :
            messages.info(request=request,message="Invalide Creidentials")
            return redirect("login")
            
    return render(request, "login.html")



def welcome(request):
    return render(request, "welcome.html")
