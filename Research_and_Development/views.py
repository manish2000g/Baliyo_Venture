from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import ResearchAndDevelopment, ResearchAndDevelopmentDetail
from .serializers import RDSerializer, RDetailSerializer
# Create your views here.
@api_view(["GET"])
def RDevelopment(request):
    rdevelopment = ResearchAndDevelopment.objects.all()
    serializer = RDSerializer(rdevelopment, many = True)
    return Response(serializer.data)


@api_view(["GET"])
def RD_Detail(request, slug):
    try:
        rd_detail = ResearchAndDevelopmentDetail.objects.get(slug=slug)
        serializer = RDetailSerializer(rd_detail)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

