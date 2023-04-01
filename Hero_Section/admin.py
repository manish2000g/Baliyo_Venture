from django.contrib import admin
from .models import HeroSections, Testimonial
from solo.admin import SingletonModelAdmin

admin.site.register(HeroSections, SingletonModelAdmin)
admin.site.register(Testimonial)

