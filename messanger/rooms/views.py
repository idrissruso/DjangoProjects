from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def chat(request,room):
    return render(request,'chat.html')

def room(request):
    return render(request,'rooms.html')
