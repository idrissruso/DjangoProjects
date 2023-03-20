from django.shortcuts import render,redirect
from .models import Posts


# Create your views here.
def home(request):
    posts = Posts.objects.all()
    return render(request,'index.html',{"posts" : posts})

def addPost(request):
    if request.method == "POST":
        data = request.POST
        post = Posts(title = data["title"],author = data["author"],content = data["content"])
        post.save()
        return redirect("home")
    return render(request,'newpost.html')

def post(request,id):
    return render(request,'post.html')