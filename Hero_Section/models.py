from django.db import models
from ckeditor.fields import RichTextField

class HeroSections(models.Model):
    title = RichTextField(max_length=200)
    hero_image = models.ImageField(upload_to= 'static/images')

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200,blank=True)
    image = models.ImageField(blank=True)
    review = models.TextField(blank=True)
    rating = models.FloatField(default=5)
    TRUSTPILOT = 'Trustpilot'
    GOOGLE = 'Google'
    OTHERS = 'Others'
    SOURCE_CHOICES = [
        (TRUSTPILOT, 'Trustpilot'),
        (GOOGLE, 'Google'),
        (OTHERS, 'Others'),
    ]
    source = models.CharField(max_length=30, choices=SOURCE_CHOICES)

    def __str__(self):
        return self.name
    

# testimonials : 
# source [ Trustpilot, Google, Others ]

