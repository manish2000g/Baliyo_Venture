from django.urls import path
from .views import HeroSection, ServiceList, PortfolioList

urlpatterns = [
    path('', HeroSection, name= 'hero_section'),
    path('servicelist/', ServiceList, name = 'servicelist'),
    path('portfoliolist/', PortfolioList, name = 'portfoliolist')
]