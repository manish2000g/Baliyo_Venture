from rest_framework import serializers
from .models import HeroSections, ServicesSec, ServiceLists, PortfolioLists

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSections
        fields = '__all__'
        


class ServiceSecSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesSec
        fields = ('__all__')


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceLists
        fields = '__all__'


class PortfolioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioLists
        fields = '__all__'
