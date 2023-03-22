from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Service
from .serializers import ServiceSerializer
# Create your views here.
@api_view(["GET"])
def Services(request):
    service = Service.objects.all()
    serializer = ServiceSerializer(service, many = True)
    return Response(serializer.data)
