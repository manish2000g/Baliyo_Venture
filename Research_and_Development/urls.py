from django.urls import path
from .views import RDevelopment

urlpatterns = [
    path('rdevelopment/', RDevelopment, name= 'rdevelopment'),
]
    