from django.urls import path
from .views import RDevelopment, RD_Detail

urlpatterns = [
    path('rdevelopment/', RDevelopment, name= 'rdevelopment'),
    path('rdevelopment/<str:slug>/', RD_Detail, name='rdevelopment_detail')
]
    