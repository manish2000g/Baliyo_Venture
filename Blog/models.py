from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Authors(models.Model):
    author_name = models.CharField(max_length=100, null=True, blank=True, help_text="<strong>Name</strong>")
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name
    
class ArticleCategory(models.Model):
    c_name = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.c_name

class Article(models.Model):
    image = models.ImageField(upload_to='static/images')
    title = RichTextField(max_length=200)
    description = models.TextField(max_length=500)
    c_name = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, null=True, blank=True,)
    author_name = models.ForeignKey(Authors, null=True, blank=True, on_delete=models.CASCADE)
    time_to_read = models.PositiveSmallIntegerField(default=False, null=True, blank=True)
    date = models.DateField()
    is_featured = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.title




