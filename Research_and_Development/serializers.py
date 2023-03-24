from rest_framework import serializers
from . models import ResearchAndDevelopment, ResearchAndDevelopmentDetail

class RDSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchAndDevelopment
        fields = '__all__'

class RDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchAndDevelopmentDetail
        fields = '__all__'