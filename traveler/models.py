from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class Destination(models.Model):

    name = models.CharField(max_length=100)
    photo_url = models.TextField()
    description = models.TextField()
    food = models.CharField(max_length=100)
    landmarks = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='destinations')
    def __str__(self):
        return self.name