from django.shortcuts import render
from rest_framework.response import Response
from .models import Portfolio
from .serializers import PortfolioSerializer
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


