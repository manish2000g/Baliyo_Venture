
from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class ResearchAndDevelopment(models.Model):
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='static/images')
    title = models.CharField(max_length=100)
    description = tinymce_models.HTMLField(max_length=500)

    def __str__(self):
        return self.title
