from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Service
from .serializers import ServiceSerializer, ServiceDetailSerializer
from rest_framework import status

# Create your views here.
@api_view(["GET"])
def Services(request):
    service = Service.objects.all()
    serializer = ServiceSerializer(service, many = True)
    return Response(serializer.data)


@api_view(["GET"])
def Service_Detail(request, slug):
    try:
        service_detail = Service.objects.get(slug=slug)
        serializer = ServiceDetailSerializer(service_detail)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


