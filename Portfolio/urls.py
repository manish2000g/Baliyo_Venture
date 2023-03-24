from django.urls import path
from .views import portfolio_by_category, portfolio_detail

urlpatterns = [
    path('portfolios/', portfolio_by_category, name= 'portfolios'),
    path('portfolios/<str:slug>/', portfolio_detail, name = 'porfolio_detail')
]