from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html',{"posts" : [1,2,3,4,5]})