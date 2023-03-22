from django.shortcuts import render
from rest_framework.response import Response
from .models import Article, Authors
from .serializers import ArticleSerializer, AuthorSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET"])
def Articles(request):
    # get all featured articles
    featured_articles = Article.objects.filter(is_featured=True)
    featured_articles_serializer = ArticleSerializer(featured_articles, many=True)

    # get all popular articles
    popular_articles = Article.objects.filter(is_popular=True)
    popular_articles_serializer = ArticleSerializer(popular_articles, many=True)

    # return response with serialized data
    return Response({
        "featured_articles": featured_articles_serializer.data,
        "popular_articles": popular_articles_serializer.data
    })


@api_view(["GET"])
def Author(request):
    author = Authors.objects.all()
    serializer = AuthorSerializer(author, many = True)
    return Response(serializer.data)
