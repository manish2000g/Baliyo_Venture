from django.urls import path
from .views import Articles, Author

urlpatterns = [
    path('article/', Articles, name= 'article'),
    path('author/', Author, name='author')
    
]