from django.urls import path
from . import views

urlpatterns = [
    path('', views.country_list, name='country_list'),
    path('countries/<int:pk>', views.country_detail, name='country_detail'),
    path('countries/new', views.country_new, name='country_create'),
    path('countries/<int:pk>/delete', views.country_delete, name='country_delete'),
    path('destinations/', views.destination_list, name='destination_list'),
    path('destinations/<int:pk>', views.destination_detail, name='destination_detail'),
    path('destinations/new', views.destination_new, name='destination_create'),
    path('destinations/<int:pk>/delete', views.destination_delete, name='destination_delete'),


]