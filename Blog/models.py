from django.db import models
from ckeditor.fields import RichTextField
from tinymce import models as tinymce_models

# Create your models here.

class Authors(models.Model):
    author_name = models.CharField(max_length=100, help_text="<strong>Name</strong>")
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name
    

class ArticleCategory(models.Model):
    c_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.c_name


class Article(models.Model):
    slug = models.SlugField(unique=True)
    thumbnail_image = models.ImageField(upload_to='static/images')
    title = RichTextField(max_length=200)
    article_content = tinymce_models.HTMLField(max_length=500) 
    c_name = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE)
    author_name = models.ForeignKey(Authors, on_delete=models.CASCADE)
    time_to_read = models.PositiveSmallIntegerField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    meta_title = models.CharField(max_length=200)
    meta_description = models.TextField(max_length=400)


    def __str__(self):
        return self.title




