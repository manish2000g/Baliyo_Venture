from .models import HeroSections, ServicesSec, ServiceLists, PortfolioLists
from .serializers import HeroSectionSerializer, ServiceSecSerializer, ServiceListSerializer, PortfolioListSerializer
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view)


@api_view(["GET"])
def HeroSection(request):
    hero_section = HeroSections.objects.all()
    serializer = HeroSectionSerializer(hero_section, many=True)

    services = ServicesSec.objects.all()
    ser_serializer = ServiceSecSerializer(services, many=True)
    return Response(
        {
        "herr_section":serializer.data,
        "services":ser_serializer.data,
        }
    )


@api_view(["GET"])
def ServiceList(request):
    service_list = ServiceLists.objects.all()
    serializer = ServiceListSerializer(service_list, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def PortfolioList(request):
    portfoliolist = PortfolioLists.objects.all()
    serializer = PortfolioListSerializer(portfoliolist, many=True)
    return Response(serializer.data)







