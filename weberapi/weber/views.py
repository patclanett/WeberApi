# todos/views.py
from rest_framework import generics

from .models import Villager
from .serializers import VillagerSerializer

class ListVillager(generics.ListCreateAPIView):
    queryset = Villager.objects.all()
    serializer_class = VillagerSerializer

class DetailVillager(generics.RetrieveUpdateDestroyAPIView):
    queryset = Villager.objects.all()
    serializer_class = VillagerSerializer