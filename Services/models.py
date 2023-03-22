from django.db import models

# Create your models here.

class Service(models.Model):
    image = models.ImageField(upload_to='static/images')
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title
