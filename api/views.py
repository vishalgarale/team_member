from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import TeamMember
from .serializers import TeamMemberSerializer
from django.db import connection

# Create your views here.


class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
