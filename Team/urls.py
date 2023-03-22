from django.urls import path
from .views import Teams

urlpatterns = [
    path('teams/', Teams, name= 'teams'),
]
    