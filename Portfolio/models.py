from django.db import models
from Services.models import Service
# Create your models here.
    
class Portfolio(models.Model):
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='static/images')
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Service, on_delete=models.CASCADE)
    description = models.TextField()
    company_name = models.CharField(max_length=100)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title

      