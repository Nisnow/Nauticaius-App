from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NpcSerializer
from .models import Npc

class NpcView(viewsets.ModelViewSet):

    serializer_class = NpcSerializer
    queryset = Npc.objects.all()