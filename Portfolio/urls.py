from django.urls import path
from .views import portfolio_by_category

urlpatterns = [
    path('portfolios/', portfolio_by_category, name= 'portfolios'),
]