from rest_framework import serializers
from . models import ResearchAndDevelopment

class RDSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchAndDevelopment
        fields = '__all__'