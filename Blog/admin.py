from django.contrib import admin
from.models import Article, Authors,ArticleCategory
# Register your models here.
admin.site.register(Article)
admin.site.register(Authors)
admin.site.register(ArticleCategory)