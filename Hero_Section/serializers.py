from rest_framework import serializers
from .models import HeroSections, Testimonial
from Services.models import Service
class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSections
        fields = '__all__'
        

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['slug', 'title'] 