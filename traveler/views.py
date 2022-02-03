from django.shortcuts import render, redirect


# Create your views here.
from rest_framework import generics
from .serializers import CountrySerializer, DestinationSerializer
from .models import Country, Destination

class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class DestinationList(generics.ListCreateAPIView): 
    queryset = Destination.objects.all() 
    serializer_class = DestinationSerializer

class DestinationDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Destination.objects.all() 
    serializer_class = DestinationSerializer 