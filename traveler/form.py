# tunr/forms.py
from django import forms
from .models import Country, Destination

class CountryForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = ('name', 'photo_url',)

class DestinationForm(forms.ModelForm):

    class Meta:
        model = Destination
        fields = ('name', 'photo_url', 'description', 'food', 'landmarks', 'cost', 'country',)