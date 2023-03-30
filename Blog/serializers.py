from rest_framework import serializers
from . models import Article, Authors

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['thumbnail_image', 'title', 'article_content', 'time_to_read', 'is_featured', 'is_popular']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
