from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.home),
    path('login/', view=views.login),
    path('login/welcome', view=views.welcome)
]
