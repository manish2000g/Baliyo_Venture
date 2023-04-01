from .models import HeroSections, Testimonial
from Portfolio.models import Portfolio
from Services.models import Service
from Services.serializers import ServiceSerializer
from Portfolio.serializers import PortfolioSerializer
from .serializers import HeroSectionSerializer, TestimonialSerializer, ServiceListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def HeroSection(request):
    try:
        hero_section = HeroSections.objects.get()
        serializer = HeroSectionSerializer(hero_section)
    except HeroSections.DoesNotExist:
        serializer = HeroSectionSerializer()

    services = Service.objects.all()
    ser_serializer = ServiceListSerializer(services, many=True)

    testimonials = Testimonial.objects.all()
    test_serializer = TestimonialSerializer(testimonials, many=True)

    return Response({
        "hero_section": serializer.data,
        "services": ser_serializer.data,
        "testimonials": test_serializer.data,
    })


@api_view(["GET"])
def ServiceList(request):
    service_list = Service.objects.all()
    serializer = ServiceSerializer(service_list, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def PortfolioList(request):
    portfoliolist = Portfolio.objects.all()
    serializer = PortfolioSerializer(portfoliolist, many=True)
    return Response(serializer.data)







