from django.urls import path
from .views import Services

urlpatterns = [
    path('services/', Services, name= 'services'),
]
    