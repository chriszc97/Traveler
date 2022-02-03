
# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Country
from .models import Location

admin.site.register(Country)
admin.site.register(Location)