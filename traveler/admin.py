
# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Country
from .models import Destination

admin.site.register(Country)
admin.site.register(Destination)