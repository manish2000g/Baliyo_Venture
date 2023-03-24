from rest_framework import serializers
from .models import HeroSections, Testimonial

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSections
        fields = '__all__'
        

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'