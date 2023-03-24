from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name = "home"),
    path('login/',views.login_view,name = 'login'),
    path('register/',views.register,name = 'register'),
    path('room/',views.rooms,name = 'rooms'),
    path('room/new_room/',views.new_room,name = 'new_room'),
    path('room/chat/<str:room>',views.chat,name = 'chat')
    
]
