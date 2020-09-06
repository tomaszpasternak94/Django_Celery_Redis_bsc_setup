from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=64, unique=True)
    temperature = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    icon = models.CharField(max_length=64, null=True, blank=True)
    country = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self):
        return self.name