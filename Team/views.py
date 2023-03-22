from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Team
from .serilaizers import TeamSerializer
# Create your views here.
@api_view(["GET"])
def Teams(request):
    team = Team.objects.all()
    serializer = TeamSerializer(team, many = True)
    return Response(serializer.data)
