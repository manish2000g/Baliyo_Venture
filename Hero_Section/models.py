from django.db import models
from ckeditor.fields import RichTextField

class HeroSections(models.Model):
    title = RichTextField(max_length=200)
    hero_image = models.ImageField(upload_to= 'static/images')

    def __str__(self):
        return self.title


class Testimonial(models.Model):
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
        return self.source
    

# testimonials : 
# source [ Trustpilot, Google, Others ]

