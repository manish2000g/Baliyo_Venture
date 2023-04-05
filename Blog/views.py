from django.shortcuts import render
from rest_framework.response import Response
from .models import Article, Authors, Tag
from .serializers import ArticleSerializer, AuthorSerializer,  ArticleDetailSerializer, TagSerializer
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(["GET"])
def Articles(request):
    # get all featured articles
    featured_articles = Article.objects.filter(is_featured=True)
    featured_articles_serializer = ArticleSerializer(featured_articles, many=True)
    # get all popular articles
    popular_articles = Article.objects.filter(is_popular=True)
    popular_articles_serializer = ArticleSerializer(popular_articles, many=True)
    tags = Tag.objects.all()
    tag_serializer = TagSerializer(tags, many=True)

    return Response({
        "featured_articles": featured_articles_serializer.data,
        "popular_articles": popular_articles_serializer.data,
        "tags":tag_serializer.data
    })

@api_view(["GET"])
def featured_and_popular_articles(request):
    featured_articles = Article.objects.filter(is_featured=True).order_by('-id')[:3]
    popular_articles = Article.objects.filter(is_popular=True).order_by('-created_at')[:3]

    featured_articles_data = [ArticleSerializer(article).data for article in featured_articles]
    popular_articles_data = [ArticleSerializer(article).data for article in popular_articles]

    return Response({
        "featured_articles": featured_articles_data,
        "popular_articles": popular_articles_data
    })

@api_view(["GET"])
def featured_articles(request):
    featured_articles = Article.objects.filter(is_featured=True).order_by('-id')[:5]
    featured_articles_data = [ArticleSerializer(article).data for article in featured_articles]
    return Response({'featured_articles': featured_articles_data})

@api_view(["GET"])
def popular_articles(request):
    popular_articles = Article.objects.all().order_by('-created_at')[:5]
    popular_articles_data = [ArticleSerializer(article).data for article in popular_articles]
    return Response(popular_articles_data)

@api_view(["GET"])
def Author(request):
    author = Authors.objects.all()
    serializer = AuthorSerializer(author, many = True)
    return Response(serializer.data)


@api_view(["GET"])
def Article_Detail(request, slug):
    try:
        article_detail = Article.objects.get(slug=slug)
        serializer = ArticleDetailSerializer(article_detail)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)



