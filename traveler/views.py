from django.shortcuts import render

# Create your views here.
from .models import Country, Destination

def country_list(request):
    countries = Country.objects.all()
    return render(request, 'traveler/country_list.html', {'countries': countries})

def country_detail(request, pk):
    country = Country.objects.get(id=pk)
    return render(request, 'traveler/country_detail.html', {'country': country})

def country_new(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            country = form.save()
        return redirect('country_detail', pk=country.pk)
    else:
        form = CountryForm()
    return render(request, 'traveler/country_form.html', {'form': form})


def country_delete(request, pk):
    Country.objects.get(id=pk).delete()
    return redirect('country_list')


def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'traveler/destination_list.html', {'destinations': destinations})


def destination_detail(request, pk):
    destination = Destination.objects.get(id=pk)
    return render(request, 'traveler/destination_detail.html', {'destination': destination})


def destination_new(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            destination = form.save() 
            return redirect('destination_detail', pk=destination.pk)
    else:
        form = DestinationForm()
    return render(request, 'traveler/destination_form.html', {'form': form})


def destination_delete(request, pk):
    Destination.objects.get(id=pk).delete()
    return redirect('destination_list')
