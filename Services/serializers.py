from rest_framework import serializers
from . models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['image', 'title']

class ServiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

