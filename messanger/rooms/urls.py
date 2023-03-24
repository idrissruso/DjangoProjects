from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name = "home"),
    path('login/',views.login,name = 'login'),
    path('register/',views.register,name = 'register'),
    path('room/',views.room,name = 'room'),
    path('room/chat/<str:room>',views.chat,name = 'chat')
    
]
