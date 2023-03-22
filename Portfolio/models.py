from django.db import models
from Services.models import Service
# Create your models here.

class PortfolioCategory(models.Model):
    category = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.category.title
    

class Portfolio(models.Model):
    image = models.ImageField(upload_to='static/images')
    title = models.CharField(max_length=100)
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE)
    description = models.TextField()
    company_name = models.CharField(max_length=100,  null=True, blank=True  )
    link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title