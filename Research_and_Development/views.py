from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ResearchAndDevelopment
from .serializers import RDSerializer
# Create your views here.
@api_view(["GET"])
def RDevelopment(request):
    rdevelopment = ResearchAndDevelopment.objects.all()
    serializer = RDSerializer(rdevelopment, many = True)
    return Response(serializer.data)
