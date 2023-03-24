from django.urls import path
from .views import Services, Service_Detail

urlpatterns = [
    path('services/', Services, name= 'services'),
    path('services/<str:slug>/', Service_Detail, name='service_detail'),
]
    