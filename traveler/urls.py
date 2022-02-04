from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('countries/', views.CountryList.as_view(), name='country_list'),
    path('countries/<int:pk>', views.CountryDetail.as_view(), name='country_detail'),
    path('destinations/', views.DestinationList.as_view(), name="destination_list"),
    path('destinations/<int:pk>', views.DestinationDetail.as_view(), name="destination_detail")

]