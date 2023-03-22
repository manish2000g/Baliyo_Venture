from rest_framework import serializers
from .models import Portfolio, PortfolioCategory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioCategory
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'
    
    