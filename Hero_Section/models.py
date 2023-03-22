from django.db import models
from Portfolio.models import Portfolio, PortfolioCategory
from Services.models import Service
class HeroSections(models.Model):
    title = models.CharField(max_length=100)
    hero_image = models.ImageField(upload_to= 'static/images')

    def __str__(self):
        return self.title

class ServicesSec(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    link = models.URLField()

    def __str__(self):
        return self.service.title
    
class ServiceLists(models.Model):
    image = models.ImageField(upload_to='static/images')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.service.title

class PortfolioLists(models.Model):
    image = models.ImageField(upload_to='static/images')
    portfolio_title = models.ForeignKey(Portfolio, on_delete=models.CASCADE, null=True, blank=True, related_name='portfolio_lists_title')
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE, null=True, blank=True )
    company = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.portfolio_title.title
    


