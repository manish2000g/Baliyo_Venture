from django.urls import path
from .views import Articles, Author, Article_Detail, featured_and_popular_articles, featured_articles, popular_articles

urlpatterns = [
    path('article/', Articles, name= 'article'),
    path('article/<str:slug>/', Article_Detail, name = 'article_details'),
    path('featured_and_popular/', featured_and_popular_articles, name = 'featured_and_popular'),
    path('featured/', featured_articles, name='featured'),
    path('popular/', popular_articles,name='popular'),
    path('author/', Author, name='author')
    
]