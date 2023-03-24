from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import Portfolio
from .serializers import PortfolioSerializer, PortfolioDetailSerializer
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def portfolio_by_category(request, category_id=None):
    if category_id:
        portfolios = Portfolio.objects.filter(category__id=category_id)
    else:
        portfolios = Portfolio.objects.all()
    serializer = PortfolioSerializer(portfolios, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def portfolio_detail(request, slug):
    try:
        portfolio_detail = Portfolio.objects.get(slug=slug)
        serializer = PortfolioDetailSerializer(portfolio_detail)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

