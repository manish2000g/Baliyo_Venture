from django.db import models
from django.core.validators import EmailValidator

# Create your models here.
class Team(models.Model):
    image = models.ImageField(upload_to='static/images', default='static/images/chaur.jpg')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    post = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator(message="Invalid email address")])
    department = models.CharField(max_length=100, help_text='Department of team member')
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    

    def __str__(self):
        return self.name
