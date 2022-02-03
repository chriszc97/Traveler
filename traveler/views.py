from django.shortcuts import render

# Create your views here.
from .models import Country, Destination

def country_list(requst):
    countries = Country.objects.all()
    return render(request, 'traveler/country_list.html', {'countries': countries})

def destination_list(request):