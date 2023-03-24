from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.

def home(request):
    return render(request,'index.html')

def login_view(request):
    if request.method == "POST" :
        data = request.POST
        user = authenticate(username = data["username"],password = data["password"])
        if user is not None:
            login(request,user)
            return redirect('rooms')
        else:
            messages.info(request,"İnvalid credentials")
    return render(request,'login.html')

def register(request):
    if request.method == "POST" : 
        data = request.POST
        if data["password"] == data["c_password"]:
            if User.objects.filter(username = data["username"]).exists():
                messages.info(request,"User Name Alredy in User")
                return redirect("register")
            elif User.objects.filter(email = data["email"]).exists():
                messages.info(request,"Email Alredy in User Login if you have an acount")
                return redirect("register")
            else :
                user = User.objects.create_user(username=data["username"],email=data["email"],password=data["password"])
                user.save()
                return render(request,"login.html")
        else:
            messages.info(request,"Password Not Matched")
            return redirect("register")
    return render(request,'register.html')

def chat(request,room):
    return render(request,'chat.html')


@login_required
def rooms(request):
    rooms_ = models.Room.objects.all()
    return render(request,'rooms.html',{"rooms" : rooms_})

def new_room(request):
    if request.method == "POST":
        data = request.POST
        room = models.Room(name = data["name"],description = data["description"])
        room.save()
        return redirect("rooms")
    return render(request,'new_room.html')
