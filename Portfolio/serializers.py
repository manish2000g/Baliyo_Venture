from rest_framework import serializers
from .models import Portfolio

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['slug', 'image', 'title', 'company_name']
    
class PortfolioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'