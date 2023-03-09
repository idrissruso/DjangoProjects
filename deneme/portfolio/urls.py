from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.home),
    path('welcome/', view=views.welcome)
]
