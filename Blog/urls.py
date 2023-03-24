from django.urls import path
from .views import Articles, Author, Article_Detail

urlpatterns = [
    path('article/', Articles, name= 'article'),
    path('article_details/<str:slug>/', Article_Detail, name = 'article_details'),
    path('author/', Author, name='author')
    
]