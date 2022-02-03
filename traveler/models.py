from django.db import models

# Create your models here.

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Destination(models.Model):
     country= models.ForeignKey(Country, on_delete=models.CASCADE, related_name='destinatoin')
     name = models.CharField(max_length=100)
     photo_url = models.TextField(blank=True)
     description= models.TextField()
     food= models.CharField(max_length=100)
     landmarks = models.CharField(max_length=100)
     cost = models.CharField(max_length=100)

     def __str__(self):
        return self.name