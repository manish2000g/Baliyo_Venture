from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Service(models.Model):
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='static/images')
    title = models.CharField(max_length=100)
    description = RichTextField(max_length=500)

    def __str__(self):
        return self.title

