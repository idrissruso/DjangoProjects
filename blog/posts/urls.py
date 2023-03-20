from django.urls import path
from . import views

urlpatterns = [
    path('',view=views.home,name="home"),
    path('new_post/',views.addPost,name = "new_post"),
    path('post/<int:id>',views.post,name = "post")
    
]
